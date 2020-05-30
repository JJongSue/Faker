import os
import numpy as np
import tensorflow as tf
import json
from datasets import data as dataset
from models.nn import DCGAN as GAN
# from learning.optimizers import AdamOptimizer as Optimizer
from learning.optimizers import MomentumOptimizer as Optimizer
from learning.evaluators import FIDEvaluator as Evaluator

""" 1. Load and split datasets """
root_dir = os.path.join('data/FFHQ/') # FIXME
# root_dir = os.path.join('data/celeba-dataset/img_align_celeba') # FIXME
trainval_dir = os.path.join(root_dir, 'thumbnails128x128')
# trainval_dir = os.path.join(root_dir, 'img_align_celeba')

# Set image size and number of class
IM_SIZE = (64, 64)

# Load trainval set and split into train/val sets
X_trainval = dataset.read_data(trainval_dir, IM_SIZE, 96)
trainval_size = X_trainval.shape[0]
train_set = dataset.Dataset(X_trainval)
print(train_set.num_examples)

""" 2. Set training hyperparameters"""
hp_d = dict()

save_dir = './DCGAN_training_FFHQ_z_100_96crop_05_dense/'

# FIXME: Training hyperparameters
hp_d['batch_size'] = 64
hp_d['num_epochs'] = 100
hp_d['init_learning_rate'] = 2e-4
hp_d['momentum'] = 0.5
hp_d['learning_rate_patience'] = 10
hp_d['learning_rate_decay'] = 1.0
hp_d['eps'] = 1e-8
hp_d['score_threshold'] = 1e-4
hp_d['inception_path'] = 'inception/inception_v3_fr.pb'
hp_d['dataset_stats_path'] = os.path.join(trainval_dir, 'stats.pkl')
hp_d['eval_sample_size'] = 10000
hp_d['sample_H'] = 20
hp_d['sample_W'] = 16
hp_d['sample_dir'] = save_dir
hp_d['batch_size_eval'] = 50
hp_d['z_dim'] = 100
hp_d['G_FC_layer_channel'] = 512
hp_d['G_channel'] = 64
hp_d['D_channel'] = 64


""" 3. Build graph, initialize a session and start training """
graph = tf.get_default_graph()
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.visible_device_list = '3'
model = GAN([IM_SIZE[0], IM_SIZE[1], 3], **hp_d)

evaluator = Evaluator()
optimizer = Optimizer(model, train_set, evaluator, **hp_d)

if not os.path.exists(save_dir):
	os.mkdir(save_dir)

with open(os.path.join(save_dir, 'hyperparam.json'), 'w') as f:
	json.dump(hp_d, f, indent='\t')
	
sess = tf.Session(graph=graph, config=config)
train_results = optimizer.train(sess, save_dir=save_dir, details=True, verbose=True, **hp_d)