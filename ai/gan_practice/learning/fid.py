import os
import numpy as np
import tensorflow as tf
import pickle as pkl
import scipy.linalg as linalg
import datasets.data as dataset

class FID(object):
	"""class for calculate Frechet Inception Distance"""
	def __init__(self, model_path, dataset_stats_path, sess):
		"""
		FID initializer
		model can be download with url : 
		:param model_path : str, path of Inception model(*.pb) that calculate FID
		:param dataset_path : Dataset object, dataset to calculate m_w and C_w
		:param sess : tf.Session, session that feature extraction will be done using inception network
		"""
		self.inception_layer = self.get_inception_layer(sess, model_path)
		self.mu_data, self.sigma_data = self.get_data_stats(dataset_stats_path)
		self.sess = sess
		self.feature_gen = np.empty((0, 2048)) # 2048 is feature size of inception network
		
		
	def get_inception_layer(self, sess, model_path):
		try:
			pool_layer = sess.graph.get_tensor_by_name("FID/InceptionV3/Logits/AvgPool_1a_8x8/AvgPool:0")
		except KeyError:
			with tf.gfile.FastGFile(model_path, 'rb') as f:
				graph_def = tf.GraphDef()
				graph_def.ParseFromString(f.read())
				_ = tf.import_graph_def(graph_def, name="FID")
			pool_layer = sess.graph.get_tensor_by_name("FID/InceptionV3/Logits/AvgPool_1a_8x8/AvgPool:0")
        
		ops = pool_layer.graph.get_operations()
        
		for op_idx, op in enumerate(ops):
			for o in op.outputs:
				shape = o.get_shape()
				if shape._dims != [] and (shape._dims is not None):
					shape = [s.value for s in shape]
					new_shape = []
					for j, s in enumerate(shape):
						if s == 1 and j == 0:
							new_shape.append(None)
						else:
							new_shape.append(s)
					o.__dict__['_shape_val'] = tf.TensorShape(new_shape)
        
		return pool_layer
    
	def get_data_stats(self, dataset_stats_path):
		assert os.path.exists(dataset_stats_path)
        
		with open(dataset_stats_path, 'rb') as f:
			stats = pkl.load(f)
        
		return stats["mu"], stats["sigma"]
    
	def reset_FID(self):
		self.feature_gen = np.empty((0, 2048))
    
	def extract_inception_features(self, images):
		batch_size = images.shape[0]
		images = (images+1) * 127.5
		pred = self.sess.run(self.inception_layer, {'FID/input:0' : images})
		self.feature_gen = np.append(self.feature_gen, pred.reshape(batch_size, -1), axis=0)
    
	def calculate_FID(self):
		pred_arr = self.feature_gen
		mu = np.mean(pred_arr, axis=0)
		sigma = np.cov(pred_arr, rowvar=False)
		
		if mu.shape != self.mu_data.shape:
			print("shape of mu is {}, shape of mu_data is {}".format(mu.shape, self.mu_data.shape))
		
		assert mu.shape == self.mu_data.shape, "Training mean and Sample mean have different lengths"
		assert sigma.shape == self.sigma_data.shape, "Training cov and Sample cov have different size"

		diff = mu - self.mu_data

		cov_mean, _ = linalg.sqrtm(sigma.dot(self.sigma_data), disp=False)
		if not np.isfinite(cov_mean).all():
			print("Singular product has happened when calculate FID. adding %s to diagonal of cov estimates" % 1e-6)
			offset = np.eye(sigma.shape[0]) * 1e-6
			cov_mean = linalg.sqrtm((sigma + offset).dot(self.sigma_data + offset))
            
		if np.iscomplexobj(cov_mean):
			if not np.allclose(np.diagonal(cov_mean).imag, 0, atol=1e-3):
				m = np.max(np.abs(cov_mean.imag))
				raise ValueError("Imaginary component {}".format(m))
			cov_mean = cov_mean.real

		return np.sqrt(diff.dot(diff) + np.trace(sigma) + np.trace(self.sigma_data) - 2 * np.trace(cov_mean))
        