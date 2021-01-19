import os
import cv2
import imageio
import pydicom
import numpy as np
from tqdm import tqdm
import skimage
from skimage.morphology import ball, disk, dilation, binary_erosion, remove_small_objects, erosion, closing, reconstruction, binary_closing
from skimage.measure import label,regionprops, perimeter
from skimage.morphology import binary_dilation, binary_opening
from skimage.filters import roberts, sobel
from skimage import measure, feature
from skimage.segmentation import clear_border
from skimage.feature import greycomatrix
from sklearn.cluster import KMeans
from skimage import morphology
#from skimage.util.montage import montage2d
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
import matplotlib
from morphology import morph_filter
from skimage.draw import line
from PIL import Image

inputdir = '/home/ronn/workspace/data_base/mask/masks/COVID/MARIA ROSA DA CONCEICAO FILHA/dicom/'
#inputdir = '/home/ronn/workspace/data_base/radomica-TC-covid/HUAC - UFCG/PCT CONTROLE/Maurina Maria Alves/Maurina Maria Alves/'
input_lesion = '/home/ronn/workspace/data_base/mask/masks/COVID/MARIA ROSA DA CONCEICAO FILHA/gt/'

test_list = sorted(os.listdir (inputdir))
test_list_lesion = sorted(os.listdir (input_lesion))


folder = '030/'
output_dicom = './dataset/dicom/' + folder
output_gt = './dataset/gt/' + folder

for i in tqdm(range(len(test_list))):
    ds = pydicom.read_file( inputdir + test_list[i]) # read dicom image
    img = ds.pixel_array
    
    mask = image = cv2.imread(input_lesion + test_list_lesion[i]) # read png binary image
    
    result = lung_segmentation(img, mask)
    
    if len(result) == 2:
        '''fig, ax = plt.subplots(1, 2, figsize = [12, 12])
        ax[0].imshow(result[0], cmap="gray")
        ax[1].imshow(result[1], cmap="gray")
        ax[0].set_title(test_list[i])
        ax[1].set_title(test_list_lesion[i])'''
        
        save_dicom = test_list[i].split('.')
        save_lesion = test_list_lesion[i].split('.')
        
        imageio.imwrite(output_dicom + save_dicom[0] + ".png", result[0])
        imageio.imwrite(output_gt + save_lesion[0] + ".png", result[1])
