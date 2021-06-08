# -*- coding: utf-8 -*-
"""binarize.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18RL5q2GeLrwtHhy7eEFF4uw5fiP6sRe-
"""

def binarize(im, turn):
  """
  Binarizes a given image
  """

"""
This function takes an image and binarizes it based on a given turning point. 
Pixels with a value above the given turning point are set equal to 1 (white),
while pixels equal to or below the turning point are set equal to 0 (black). 
If the pixel values are greater than 1, the function will throw an error message.
"""

Parameters
----------
im  : 2D int array
      image
turn: int
      integer between 0 and 1
      pixel values above "turn" are set equal to 1
      pixel values equal to or below "turn" are set equal to 0

Returns
-------
err_code  : str
            prints error message if pixel value is greater than 1
binary_im : 2D int array
            binarized version of image im

def binarize(im, turn):
  w, h = im.shape
  binary_im = np.zeros((w,h)) 
  error_code = 'Error: pixel values must be between 0 and 1'

  for a,i in enumerate(im):
    for b,j in enumerate(i):
      if j>1:
        print(error_code)
      if j>turn:
        binary_im[a,b]=1
  return binary_im

Example
--------
#import numpy as np
#import scipy as sp
#import matplotlib.pyplot as plt
#from skimage.color import rgb2gray

#from google.colab import drive #used to access functions and test image
#drive.mount('/content/drive', force_remount=True)

#lily = plt.imread('/content/drive/MyDrive/testlilyslice.jpeg')
#intensity = 0.47
#lily_gr = rgb2gray(lily)

#lily_bi = binarize(lily_gr, intensity)

#titles = ['Origional', 'Binarized']
#fig, ax = plt.subplots(ncols=2, figsize=(10,6))
#ax[0].imshow(lily)
#ax[1].imshow(lily_bi, cmap='gray')

#for i,axi in enumerate(ax):
#  axi.axis('off')
#  axi.set_title(titles[i])