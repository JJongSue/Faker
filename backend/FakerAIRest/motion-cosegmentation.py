import matplotlib

matplotlib.use('Agg')

import yaml
from argparse import ArgumentParser
from tqdm import tqdm
import sys

import imageio
import numpy as np
from skimage.transform import resize
from skimage import img_as_ubyte

import torch
from sync_batchnorm import DataParallelWithCallback
import torch.nn.functional as F

from modules.segmentation_module import SegmentationModule
from modules.reconstruction_module import ReconstructionModule
from logger import load_reconstruction_module, load_segmentation_module

from modules.util import AntiAliasInterpolation2d
from modules.dense_motion import DenseMotionNetwork

def load_checkpoints(config='config/vox-256-sem-5segments.yaml', 
                checkpoint='vox-cpk.pth.tar', 
                blend_scale=0.125, 
                first_order_motion_model=False, 
                cpu=False):
    with open(config) as f:
        config = yaml.load(f)

    reconstruction_module = PartSwapGenerator(blend_scale=blend_scale,
                                              first_order_motion_model=first_order_motion_model,
                                              **config['model_params']['reconstruction_module_params'],
                                              **config['model_params']['common_params'])

    if not cpu:
        reconstruction_module.cuda()

    segmentation_module = SegmentationModule(**config['model_params']['segmentation_module_params'],
                                             **config['model_params']['common_params'])
    if not cpu:
        segmentation_module.cuda()

    if cpu:
        checkpoint = torch.load(checkpoint, map_location=torch.device('cpu'))
    else:
        checkpoint = torch.load(checkpoint)

    load_reconstruction_module(reconstruction_module, checkpoint)
    load_segmentation_module(segmentation_module, checkpoint)

    if not cpu:
        reconstruction_module = DataParallelWithCallback(reconstruction_module)
        segmentation_module = DataParallelWithCallback(segmentation_module)

    reconstruction_module.eval()
    segmentation_module.eval()

    return reconstruction_module, segmentation_module


def load_checkpoints(config, checkpoint, blend_scale=0.125, first_order_motion_model=False, cpu=False):
    with open(config) as f:
        config = yaml.load(f)

    reconstruction_module = PartSwapGenerator(blend_scale=blend_scale,
                                              first_order_motion_model=first_order_motion_model,
                                              **config['model_params']['reconstruction_module_params'],
                                              **config['model_params']['common_params'])

    if not cpu:
        reconstruction_module.cuda()

    segmentation_module = SegmentationModule(**config['model_params']['segmentation_module_params'],
                                             **config['model_params']['common_params'])
    if not cpu:
        segmentation_module.cuda()

    if cpu:
        checkpoint = torch.load(checkpoint, map_location=torch.device('cpu'))
    else:
        checkpoint = torch.load(checkpoint)

    load_reconstruction_module(reconstruction_module, checkpoint)
    load_segmentation_module(segmentation_module, checkpoint)

    if not cpu:
        reconstruction_module = DataParallelWithCallback(reconstruction_module)
        segmentation_module = DataParallelWithCallback(segmentation_module)

    reconstruction_module.eval()
    segmentation_module.eval()

    return reconstruction_module, segmentation_module