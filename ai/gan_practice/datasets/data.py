import os
import numpy as np
from cv2 import imread, resize
import glob

IMAGE_EXTS = ["jpg", "png", "bmp"]

def read_data(data_dir, image_size, crop_size=None):
    """
    Load data for GAN training
    :param data_dir : str, path to the directory to read.
    image_size : tuple (width, height), value for resizing input image
    :return: X_set : np.ndarray, shape: (N, H, W, C).
    """
    img_list = [img for img in os.listdir(data_dir) if img.split(".")[-1] in IMAGE_EXTS]
    images = []
    
    for img in img_list:
        img_path = os.path.join(data_dir, img)
        im = imread(img_path)
        im = np.array(im, dtype=np.float32)
        if crop_size:
            im = center_crop(im, crop_size, crop_size)
        else:
            im = resize(im, (image_size[1], image_size[0]))
        if len(im.shape) == 2:
            im = np.expand_dims(im, 2)
        else:
            im = im[:,:,::-1]
        im = im/127.5 - 1
        images.append(im)
        
    X_set = np.array(images, dtype=np.float32)
    
    return X_set


def read_data_batch(data_dir, img_list, image_size, crop_size=None):
    images = []
    
    for img in img_list:
        img_path = os.path.join(data_dir, img)
        im = imread(img_path)
        im = np.array(im, dtype=np.float32)
        if crop_size:
            im = center_crop(im, crop_size, crop_size, image_size[0], image_size[1])
        else:
            im = resize(im, (image_size[1], image_size[0]))
        if len(im.shape) == 2:
            im = np.expand_dims(im, 2)
            im = np.concatenate([im, im, im], -1)
        im = im/127.5 - 1
        im = im[:,:,::-1]
        images.append(im)
        
    X_set = np.array(images, dtype=np.float32)
    
    return X_set


def center_crop(x, crop_h, crop_w, resize_h=64, resize_w=64):
    if crop_w is None:
        crop_w = crop_h
    h, w = x.shape[:2]
    j = int(round((h - crop_h)/2.))
    i = int(round((w - crop_w)/2.))
    return resize(x[j:j+crop_h, i:i+crop_w], (resize_h, resize_w))


class Dataset(object):
    
    def __init__(self, images):
        """
        Construct a new Dataset object.
        :param images : np.ndarray, (N, H, W, C)
        """
        self._num_examples = images.shape[0]
        self._images = images
        self._indices = np.arange(self._num_examples, dtype=np.uint)
        self._reset()
        
    def _reset(self):
        """Reset some variables."""
        self._epoch_completed = 0
        self._index_in_epoch = 0
        
    @property
    def images(self):
        return self._images
    
    @property
    def num_examples(self):
        return self._num_examples
    
    def next_batch(self, batch_size, shuffle=True):
        """
        Return the next 'batch_size' examples from this dataset.
        :param batch_size : int, size of a single batch.
        :param shuffle : bool, whether to shuffle the whole set while sampling a batch.
        :return: batch_images : np.ndarray, shape: (N,H,W,C)
        """
        
        start_index = self._index_in_epoch
        
        if self._epoch_completed == 0 and start_index == 0 and shuffle:
            np.random.shuffle(self._indices)
        
        if start_index + batch_size > self._num_examples:
            self._epoch_completed += 1
            rest_num_examples = self._num_examples - start_index
            
            indices_rest_part = self._indices[start_index:self._num_examples]
            
            if shuffle:
                np.random.shuffle(self._indices)
            
            start_index = 0
            self._index_in_epoch = batch_size - rest_num_examples
            end_index = self._index_in_epoch
            indices_new_part = self._indices[start_index:end_index]
            
            images_rest_part = self._images[indices_rest_part]
            images_new_part = self._images[indices_new_part]
            batch_images = np.concatenate(
                (images_rest_part, images_new_part), axis=0)
        else:
            self._index_in_epoch += batch_size
            end_index = self._index_in_epoch
            indices = self._indices[start_index:end_index]
            batch_images = self._images[indices]
        
        return batch_images