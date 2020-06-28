import os
import time
from abc import abstractmethod, ABCMeta
import numpy as np
import tensorflow as tf
from learning.utils import plot_learning_curve, save_sample_images
from learning.fid import FID

class Optimizer(metaclass=ABCMeta):
	"""Base class for gradient-based optimization algorithms."""

	def __init__(self, model, train_set, evaluator, **kwargs):
		"""
		Optimizer initializer.
		:param model: Net, the model to be learned.
		:param train_set: DataSet, training set to be used.
		:param evaluator: Evaluator, for computing performance scores during training.
		:param val_set: Datset, validation set to be used, which can be None if not used.
		:param kwargs: dict, extra argument containing training hyperparameters.
			- batch_size: int, batch size for each iteration.
			- num_epochs: int, total number of epochs for training.
			- init_learning_rate: float, initial learning rate.
		"""
		self.model = model
		self.train_set = train_set
		self.evaluator = evaluator
		sample_H = kwargs.pop('sample_H', 2)
		sample_W = kwargs.pop('sample_W', 10)
		z_dim = kwargs.pop('z_dim', 100)
		self.sample_z = self.z_sample(sample_H, sample_W, z_dim)

		# Training hyperparameters
		self.batch_size = kwargs.pop('batch_size', 8)
		self.num_epochs = kwargs.pop('num_epochs', 100)
		self.init_learning_rate = kwargs.pop('init_learning_rate', 0.001)
		self.learning_rate_placeholder = tf.placeholder(tf.float32)
        
		self.optimize_G = self._optimize_op("generator")
		self.optimize_D = self._optimize_op("discriminator")

		self._reset()

	def _reset(self):
		"""Reset some variables."""
		self.curr_epoch = 1
		self.num_bad_epochs = 0	# number of bad epochs, where the model is updated without improvement.
		self.best_score = self.evaluator.worst_score	# initialize best score with the worst one
		self.curr_learning_rate = self.init_learning_rate
    
	def z_sample(self, H, W, z_dim):
		z = np.random.uniform(-1.0, 1.0, size=(W*H, z_dim))
		return z


	@abstractmethod
	def _optimize_op(self, mode, **kwargs):
		"""
		tf.train.Optimizer.minimize Op for a gradient update.
		This should be implemented, and should not be called manually.
		"""
		pass

	@abstractmethod
	def _update_learning_rate(self, **kwargs):
		"""
		Update current learning rate (if needed) on every epcoh, by its own schedule.
		This should be implemented, and should not be called manually.
		"""
		pass

	def _step(self, sess, **kwargs):
		"""
		Make a single gradient update and return its results.
		This should not be called manually.
		:param sess, tf.Session.
		:return loss: float, loss value for the single iteration step.
			y_true: np.ndarray, true label from the training set.
			y_pred: np.ndarray, predicted label from the model.
		"""

		# Sample a single batch
		X = self.train_set.next_batch(self.batch_size, shuffle=True)
		z = np.random.uniform(-1.0, 1.0, size=(self.batch_size, self.model.z_dim)) \
		.astype(np.float32)
		# Compute the loss and make update
        # Generator will be updated twice
		_, D_loss, D = \
			sess.run([self.optimize_D, self.model.discr_loss, self.model.D_l4],
				feed_dict={self.model.z: z, self.model.X: X, self.model.is_train: True, 
							self.learning_rate_placeholder: self.curr_learning_rate})
		_, G_loss, G = \
			sess.run([self.optimize_G, self.model.gen_loss, self.model.G],
				feed_dict={self.model.z: z, self.model.X: X, self.model.is_train: True, 
							self.learning_rate_placeholder: self.curr_learning_rate})
		_, G_loss, G = \
			sess.run([self.optimize_G, self.model.gen_loss, self.model.G],
				feed_dict={self.model.z: z, self.model.X: X, self.model.is_train: True, 
							self.learning_rate_placeholder: self.curr_learning_rate})
		return G_loss, D_loss, X, G, D
    
	def train(self, sess, save_dir='/tmp', details=False, verbose=True, **kwargs):
		"""
		Run optimizer to train the model.
		:param sess: tf.Session.
		:param save_dir: str, the directory to save the learned weights of the model.
		:param details: bool, whether to return detailed results.
		:param verbose: bool, whether to print details during training.
		:param kwargs: dict, extra arguments containing training hyperparameters.
			- nms_flag: bool, whether to do non maximum supression(nms) for evaluation.
		:return train_results: dict, containing detailed results of training.
		"""
		saver = tf.train.Saver()
		sess.run(tf.global_variables_initializer())	# initialize all weights
        
		inception_path = kwargs.pop('inception_path', 
                                    './inception/inception-2015-12-05/classify_image_graph_def.pb')
		dataset_stats_path = kwargs.pop('dataset_stats_path', './data/thumbnails128x128/stats.pkl')
		fid = FID(inception_path, dataset_stats_path, sess)

		train_results = dict()
		train_size = self.train_set.num_examples
		print("Size of train set :", train_size)
		num_steps_per_epoch = train_size // self.batch_size
		num_steps = self.num_epochs * num_steps_per_epoch
        
		n_eval = kwargs.pop('eval_sample_size',10000)
		batch_size_eval = kwargs.pop('batch_size_eval',500)
        
		sample_H = kwargs.pop('sample_H', 2)
		sample_W = kwargs.pop('sample_W', 10)
		sample_dir = kwargs.pop('sample_dir', save_dir)
        
		if verbose:
			print('Running training loop...')
			print('Number of training iterations: {}'.format(num_steps))

		step_losses_G, step_losses_D, step_scores, eval_scores = [], [], [], []
		start_time = time.time()

		# Start training loop
		for i in range(num_steps):
			# Perform a gradient update from a single minibatch
			step_loss_G, step_loss_D, step_X, gen_img, D = self._step(sess, **kwargs)
			step_losses_G.append(step_loss_G)
			step_losses_D.append(step_loss_D)
			# Perform evaluation in the end of each epoch
			if (i) % 10 == 0:
				print('[step {}]\tG_loss: {:.6f}|D_loss:{:.6f} |lr: {:.6f}'\
					  .format(i, step_loss_G, step_loss_D, self.curr_learning_rate))
			if (i) % num_steps_per_epoch == num_steps_per_epoch - 1:
				# Evaluate model with current minibatch, from training set
				fid.reset_FID()
				fid.extract_inception_features(gen_img)
				step_score = fid.calculate_FID()
				step_scores.append(step_score)

				sample_image = self.model.generate(sess, self.sample_z, verbose=False, **kwargs)
                
				save_sample_images(sample_dir, i, sample_image, sample_H, sample_W)
                                
				eval_score = self.evaluator.score(sess, fid, self.model, **kwargs)
				eval_scores.append(eval_score)

				if verbose:
 					# Print intermediate results
					print('[epoch {}]\tG_loss: {:.6f}|D_loss:{:.6f} |Train score: {:.6f} |Eval score: {:.6f} |lr: {:.6f}'\
						.format(self.curr_epoch, step_loss_G, step_loss_D, step_score, eval_score, self.curr_learning_rate))
					# Plot intermediate results
					plot_learning_curve(-1, step_losses_G, step_losses_D, step_scores, eval_scores=eval_scores, img_dir=save_dir)

				curr_score = eval_score

				# Keep track of the current best model,
				# by comparing current score and the best score

				if self.evaluator.is_better(curr_score, self.best_score, **kwargs):
					self.best_score = curr_score
					self.num_bad_epochs = 0
					saver.save(sess, os.path.join(save_dir, 'model_{}.ckpt'.format(self.curr_epoch)))
				else:
					self.num_bad_epochs += 1
				# Uncomment if you want to update learning rate
# 				self._update_learning_rate(**kwargs)
				self.curr_epoch += 1

		if verbose:
			print('Total training time(sec): {}'.format(time.time() - start_time))
			print('Best {} score: {}'.format('evaluation' if eval else 'training', self.best_score))

		print('Done.')

		if details:
            # Save last model
			saver.save(sess, os.path.join(save_dir, 'model.ckpt'))
			# Store training results in a dictionary
			train_results['step_losses_G'] = step_losses_G
			train_results['step_losses_D'] = step_losses_D
			train_results['step_scores'] = step_scores
			train_results['eval_scores'] = eval_scores

			return train_results

class MomentumOptimizer(Optimizer):
	"""Gradient descent optimizer, with Momentum algorithm."""

	def _optimize_op(self, mode, **kwargs):
		"""
		tf.train.MomentumOptimizer.minimize Op for a gradient update.
		:param kwargs: dict, extra arguments for optimizer.
			-momentum: float, the momentum coefficent.
		:return tf.Operation.
		"""
        
		if mode == 'generator':
			loss = self.model.gen_loss
		else:
			loss = self.model.discr_loss
        
		momentum = kwargs.pop('momentum', 0.9)
		extra_update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
		update_vars = [var for var in tf.trainable_variables() if mode in var.name]
		print("{} vars will be trained for mode {}".format(len(update_vars), mode))
		for var in update_vars:
			print("{} variable has {} shape".format(var.name, var.shape))
		with tf.control_dependencies(extra_update_ops):
			train_op = tf.train.AdamOptimizer(self.learning_rate_placeholder, momentum).minimize(loss, var_list=update_vars)
		return train_op

	def _update_learning_rate(self, **kwargs):
		"""
		Update current learning rate, when evaluation score plateaus.
		:param kwargs: dict, extra arguments for learning rate scheduling.
			- learning_rate_patience: int, number of epochs with no improvement after which learning rate will be reduced.
			- learning_rate_decay: float, factor by which the learning rate will be updated.
			-eps: float, if the difference between new and old learning rate is smller than eps, the update is ignored.
		"""
		learning_rate_patience = kwargs.pop('learning_rate_patience', 10)
		learning_rate_decay = kwargs.pop('learning_rate_decay', 0.1)
		eps = kwargs.pop('eps', 1e-8)

		if self.num_bad_epochs > learning_rate_patience:
			new_learning_rate = self.curr_learning_rate * learning_rate_decay
			# Decay learning rate only when the difference is higher than epsilon.
			if self.curr_learning_rate - new_learning_rate > eps:
				self.curr_learning_rate = new_learning_rate
			self.num_bad_epochs = 0

class AdamOptimizer(Optimizer):
	"""Gradient descent optimizer, with Momentum algorithm."""

	def _optimize_op(self, mode, **kwargs):
		"""
		tf.train.AdamOptimizer.minimize Op for a gradient update.
		:param kwargs: dict, extra arguments for optimizer.
			-momentum: float, the momentum coefficent.
		:return tf.Operation.
		"""
        
		if mode == 'generator':
			loss = self.model.gen_loss
		else:
			loss = self.model.discr_loss
            
		momentum = kwargs.pop('momentum', 0.9)
		extra_update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
		update_vars = [var for var in tf.trainable_variables() if mode in var.name]
		for var in update_vars:
			print("{} variable has {} shape".format(var.name, var.shape))
		with tf.control_dependencies(extra_update_ops):
			train_op = tf.train.AdamOptimizer(self.learning_rate_placeholder, momentum).minimize(loss, var_list=update_vars)
		return train_op

	def _update_learning_rate(self, **kwargs):
		"""
		Update current learning rate, when evaluation score plateaus.
		:param kwargs: dict, extra arguments for learning rate scheduling.
			- learning_rate_patience: int, number of epochs with no improvement after which learning rate will be reduced.
			- learning_rate_decay: float, factor by which the learning rate will be updated.
			-eps: float, if the difference between new and old learning rate is smller than eps, the update is ignored.
		"""
		learning_rate_patience = kwargs.pop('learning_rate_patience', 10)
		learning_rate_decay = kwargs.pop('learning_rate_decay', 0.1)
		eps = kwargs.pop('eps', 1e-8)

		if self.num_bad_epochs > learning_rate_patience:
			new_learning_rate = self.curr_learning_rate * learning_rate_decay
			# Decay learning rate only when the difference is higher than epsilon.
			if self.curr_learning_rate - new_learning_rate > eps:
				self.curr_learning_rate = new_learning_rate
				self.num_bad_epochs = 0