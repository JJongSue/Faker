import os
import cv2
import numpy as np
import tensorflow as tf
import json
from datasets import data as dataset
from models.nn import DCGAN as GAN
from matplotlib import pyplot as plt
from learning.utils import save_sample_images, interpolate
from learning.fid import FID

""" 1. Load training hyperparameters"""
hp_d = dict()

save_dir = './DCGAN_training_FFHQ_z_100_96crop_01/'

with open(os.path.join(save_dir, 'hyperparam.json'), 'r') as f:
    hp_d = json.load(f)
    

# Set image size
IM_SIZE = (64, 64)

""" 2. Build graph, initialize a session and load model """
graph = tf.get_default_graph()
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.visible_device_list = '1'
model = GAN([IM_SIZE[0], IM_SIZE[1], 3], **hp_d)

saver = tf.train.Saver()

sess = tf.Session(graph=graph, config=config)
saver.restore(sess, os.path.join(save_dir, 'model_94.ckpt'))

""" Test random generated image """
W = hp_d["sample_W"]
H = hp_d["sample_H"]

z = np.random.uniform(-1.0, 1.0, size=(W*H,hp_d["z_dim"]))

gen_img = model.generate(sess, z, verbose=True)
save_sample_images(save_dir, 'random', gen_img, H, W)

""" interpolate image from one to other"""
from_z = np.random.uniform(-1.0, 1.0, size=(1,hp_d["z_dim"]))
to_z = np.random.uniform(-1.0, 1.0, size=(1,hp_d["z_dim"]))

latent_intp = interpolate(from_z, to_z, 9)
img_intp = model.generate(sess, latent_intp, verbose=True)
save_sample_images(save_dir, 'interpolate_1', img_intp, 1, 11)

""" calculate FID score"""
fid = FID(hp_d["inception_path"], hp_d["dataset_stats_path"], sess)

fid.reset_FID()
sample_size = hp_d["eval_sample_size"]
sample_batch_size = hp_d['batch_size_eval']
n_batch = sample_size // sample_batch_size
for i in range(n_batch):
    eval_z = np.random.uniform(-1.0, 1.0, size=(sample_batch_size, hp_d["z_dim"]))
    g_img = model.generate(sess, eval_z)
    fid.extract_inception_features(g_img)
result = fid.calculate_FID()
print(result)