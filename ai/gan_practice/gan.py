import os
import cv2
from numpy as np


def read_data(data_dir, image_size, crop_size=None):
    """
    GAN을 학습하기 위해 데이터를 전처리하고 불러옴
    :param data_dir : str, image가 저장된 경로.
    :param image_size : tuple (width, height), 이미지를 resize할 경우 이미지 사이즈
    :param crop_size : int, 얼굴 이미지에서 배경을 제외한 얼굴만을 crop할경우 crop할 영역의 크기
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
        im = im/127.5 - 1
        im = im[:,:,::-1]
        images.append(im)
        
    X_set = np.array(images, dtype=np.float32)
    
    return X_set


class Dataset(object):
    
    def __init__(self, images):
        """
        새로운 DataSet 객체를 생성함.
        :param images : np.ndarray, (N, H, W, C)
        """
        self._num_examples = images.shape[0]
        self._images = images
        self._indices = np.arange(self._num_examples, dtype=np.uint)
        self._reset()
        
    def _reset(self):
        """일부 변수를 재설정함."""
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
        `batch_size` 개수만큼의 이미지들을 현재 데이터셋으로부터 추출하여 미니배치 형태로 반환함.
        :param batch_size : int, 미니배치 크기.
        :param shuffle : bool, 미치배치 추출에 앞서, 현재 데이터셋 내 이미지들의 순서를 랜덤하게 섞을 것인지 여부.
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