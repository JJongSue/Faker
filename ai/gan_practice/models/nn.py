import time
from abc import abstractmethod, ABCMeta
import tensorflow as tf
import numpy as np
from models.layers import conv_layer, deconv_layer, conv_bn_lrelu, deconv_bn_relu, fc_layer, fc_bn_lrelu, batchNormalization
import os

slim = tf.contrib.slim


class GAN(metaclass=ABCMeta):
    """Base class for Generative Adversarial Network"""
    
    def __init__(self, input_shape, **kwargs):
        """
        model initializer
        :param input_shape: np.array, shape [H,W,C]
        """

        if input_shape is None:
            input_shape = [None, None, 3]
        self.z_dim = kwargs.pop('z_dim', 100)
        self.c_dim = input_shape[-1]
            
        self.X = tf.placeholder(tf.float32, [None] + input_shape)
        self.z = tf.placeholder(tf.float32, [None] + [self.z_dim])
        self.is_train = tf.placeholder(tf.bool)
        
        self.G = self._build_generator(**kwargs)
        self.D, self.D_logits, self.D_l4 = self._build_discriminator(False, **kwargs)
        self.D_, self.D_logits_, _ = self._build_discriminator(True, **kwargs)
        self.G_ = self._build_sampler(**kwargs)
        
        self.gen_loss, self.discr_loss = self._build_loss(**kwargs)
        
    @abstractmethod
    def _build_generator(self, **kwargs):
        """
        Build Generator.
        This should be implemented.
        """
        pass
    
    @abstractmethod
    def _build_discriminator(self, **kwargs):
        """
        Build Discriminator.
        This should be implemented.
        """
        pass
    
    
    @abstractmethod
    def _build_loss(self, **kwargs):
        """
        Build loss function for the model training.
        It returns loss for generator and loss for discriminator.
        This should be implemented.
        """
        pass
	
    def reuse_variable(self, scope, reuse):
        if reuse:
            scope.reuse_variables()
        return 1
    
    def generate(self, sess, z, verbose=False, **kwargs):
        """
        Generate images using z vector.
        :param sess: tf.Session
        :param z: np.ndarray, (N, z_dim)
        :param verbose: bool, whether to print details during generation.
        :params kwargs: dict, extra argments for generation. 
                -batch_size: int, batch_size for iteration.
        :return _image_gen: np.ndarray, shape: shape of (N, H, W, C)
        """
        
        batch_size = kwargs.pop('batch_size', 64)
        
        num_image = z.shape[0]
        num_steps = num_image//batch_size
        
        if verbose:
            print("Running generation loop...")
        
        
        _image_gen = []
        start_time = time.time()
        for i in range(num_steps + 1):
            start_batch = i * batch_size
            
            if i==num_steps:
                _batch_size = num_image - num_steps * batch_size
            else:
                _batch_size = batch_size
            
            end_batch = start_batch + _batch_size
            z_batch = z[start_batch:end_batch]
            
            image_gen = sess.run(self.G_, feed_dict={
                                self.z : z_batch})
            _image_gen.append(image_gen)
            
        if verbose:
            print('Total generation time(sec): {}'.format(
                time.time() - start_time))
        
        _image_gen = np.concatenate(_image_gen, axis=0)
        
        return _image_gen
    
    

class DCGAN(GAN):
    """
    DCGAN class
    see: Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks
    https://arxiv.org/abs/1511.06434
    """
    def _build_generator(self, **kwargs):
        d = dict()
        c_dim = self.X.shape[-1]
        output_dim_H, output_dim_W = (self.X.shape[1],self.X.shape[2])
        kernel_size = (5,5)
        fc_channel = kwargs.pop('G_FC_layer_channel', 1024)
        G_channel = kwargs.pop('G_channel', 64)
        
        with tf.variable_scope("generator") as scope:
            z_input = self.z
            
            d['layer_1'] = fc_layer(z_input, 4*4*fc_channel)
            d['reshape'] = tf.nn.relu(batchNormalization(tf.reshape(d['layer_1'], [-1, 4, 4, fc_channel]), self.is_train))
            d['layer_2'] = deconv_bn_relu(d['reshape'], G_channel*4, kernel_size, self.is_train, strides=(2,2))
            d['layer_3'] = deconv_bn_relu(d['layer_2'], G_channel*2, kernel_size, self.is_train, strides=(2,2))
            d['layer_4'] = deconv_bn_relu(d['layer_3'], G_channel, kernel_size, self.is_train, strides=(2,2))
            d['layer_5'] = deconv_bn_relu(d['layer_4'], c_dim, kernel_size, self.is_train, strides=(2,2), bn=False, relu=False)
            d['tanh'] = tf.nn.tanh(d['layer_5'])
            
        return d['tanh']
	
    def _build_sampler(self, **kwargs):
        d = dict()
        c_dim = self.X.shape[-1]
        output_dim_H, output_dim_W = (self.X.shape[1],self.X.shape[2])
        kernel_size = (5,5)
        fc_channel = kwargs.pop('G_FC_layer_channel', 1024)
        G_channel = kwargs.pop('G_channel', 64)
        
        with tf.variable_scope("generator") as scope:
            scope.reuse_variables()
            z_input = self.z
            
            d['layer_1'] = fc_layer(z_input, 4*4*fc_channel)
            d['reshape'] = tf.nn.relu(batchNormalization(tf.reshape(d['layer_1'], [-1, 4, 4, fc_channel]), False))
            d['layer_2'] = deconv_bn_relu(d['reshape'], G_channel*4, kernel_size, False, strides=(2,2))
            d['layer_3'] = deconv_bn_relu(d['layer_2'], G_channel*2, kernel_size, False, strides=(2,2))
            d['layer_4'] = deconv_bn_relu(d['layer_3'], G_channel, kernel_size, False, strides=(2,2))
            d['layer_5'] = deconv_bn_relu(d['layer_4'], c_dim, kernel_size, False, strides=(2,2), bn=False, relu=False)
            d['tanh'] = tf.nn.tanh(d['layer_5'])
            
        return d['tanh']
    
    def _build_discriminator(self, fake_image=False, **kwargs):
        d = dict()
        kernel_size = (5,5)
        if fake_image:
            input_image = self.G
        else:
            input_image = self.X
        batch_size = kwargs.pop('batch_size', 8)
        D_channel = kwargs.pop('D_channel', 64)
        
        with tf.variable_scope("discriminator") as scope:
            if fake_image:
                scope.reuse_variables()
            
            d['layer_1'] = conv_bn_lrelu(input_image, D_channel, kernel_size, self.is_train, strides=(2,2), bn=False)
            d['layer_2'] = conv_bn_lrelu(d['layer_1'], D_channel*2, kernel_size, self.is_train, strides=(2,2))
            d['layer_3'] = conv_bn_lrelu(d['layer_2'], D_channel*4, kernel_size, self.is_train, strides=(2,2))
            d['layer_4'] = conv_bn_lrelu(d['layer_3'], D_channel*8, kernel_size, self.is_train, strides=(2,2))
            d['layer_5'] = fc_layer(tf.contrib.layers.flatten(d['layer_4']),1)
            d['sigmoid'] = tf.nn.sigmoid(d['layer_5'])
			
            
        
        return d['sigmoid'], d['layer_5'], d['layer_1']
    
    def _build_loss(self, **kwargs):
        """
        Build loss function for the model training
        :return tf.Tensor
        """
        d_loss_real = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=self.D_logits, labels=tf.ones_like(self.D)))
        d_loss_fake = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=self.D_logits_, labels=tf.zeros_like(self.D_)))
        g_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=self.D_logits_, labels=tf.ones_like(self.D_)))
        
        d_loss = d_loss_real + d_loss_fake
        return g_loss, d_loss