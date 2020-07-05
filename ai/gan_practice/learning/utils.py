import os
import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt
import cv2

def plot_learning_curve(exp_idx, step_G_losses, step_D_losses, step_scores=None, 
                        eval_scores=None, img_dir='.'):
    fig, axes = plt.subplots(2, 1, figsize=(10,10))
    axes[0].plot(np.arange(1, len(step_G_losses) + 1), step_G_losses, 
                 marker='', color='r')
    axes[0].plot(np.arange(1, len(step_D_losses) + 1), step_D_losses, 
                 marker='', color='b')
    axes[0].set_ylabel('loss')
    axes[0].set_xlabel('Number of iterations')
    if step_scores is not None:
        axes[1].plot(np.arange(1, len(step_scores) + 1), step_scores, 
					 color='b', marker='')
    if eval_scores is not None:
        axes[1].plot(np.arange(1, len(eval_scores)+1), eval_scores, 
                     color='r', marker='')
    axes[1].set_ylabel('FID')
    axes[1].set_xlabel('Number of epochs')
    
    plot_img_filename = 'learning_curve-result{}.svg'.format(exp_idx)
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    fig.savefig(os.path.join(img_dir, plot_img_filename))
    
    pkl_filename = 'learning_curve-result{}.pkl'.format(exp_idx)
    with open(os.path.join(img_dir, pkl_filename), 'wb') as fo:
        pkl.dump([step_G_losses, step_D_losses, step_scores, eval_scores], fo)
	
    plt.close(fig)
        
        
def save_sample_images(save_dir, step, sample_images, H, W):
    """
    Save sample images to grid image
    :param save_dir: str, directory to save image
    :param step: int, current_epoch
    :param H: int, grid height
    :param W: int, grid width
    """
    grid_image = []
    
    for i in range(H):
        grid_w = []
        for j in range(W):
            idx = i*W + j
            image = (sample_images[idx]+1)*127.5
            grid_w.append(image)
        grid_image_w = np.concatenate(grid_w, axis=1)
        grid_image.append(grid_image_w)
    
    grid_image = np.concatenate(grid_image, axis=0)
    
    file_name = 'sample_image_{}'.format(step) + '.jpg'
    cv2.imwrite(os.path.join(save_dir, file_name), grid_image[:,:,::-1])
    
    
def interpolate(v1, v2, W):
    diff = v2-v1
    intp = np.tile(v1, (W+2,1))
    for i in range(W+2):
        intp[i,:] += np.squeeze(diff/(W+1) * i)
    return intp