import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from skimage import io
from skimage import img_as_ubyte

path = os.getcwd()
path_gt = path + '/GT'
save_path = path + '/Edge'
os.chdir(save_path)
#os.makedirs('/test', mode = 0o777, exist_ok = True)
kernel = np.ones((5, 5), np.uint8)

print(path, path_gt)
for name in os.listdir(path_gt):
    img = io.imread(path_gt + '/' + name) 
    dilated = ndimage.binary_dilation(img) 
    dilated = img_as_ubyte(dilated)
    new = dilated - img
    io.imsave(name, new)
