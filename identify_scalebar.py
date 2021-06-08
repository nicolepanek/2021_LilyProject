# -*- coding: utf-8 -*-
"""identify_scalebar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pV0qsdJYIhF0Cu4i-CEae2J5FBOGpS0j
"""

def identify(lily_im):
  """
 identifies the separate objects in an image
  """

"""
This function was Team Lily's solution for identifying which labeled object in a 
lily mask image is the scale bar. It It skeletonizes the lily mask and labels the
separate objects within the image. The first 5 of these objects are displayed so 
the user can manually identify which is the scale bar.
Note to user: Google Colab is a great tool, but made it nearly impossible to use an interactive GUI for this step.  
"""

Parameters
----------
lily :2D by 3 int array
      RBG image

Returns
-------
"""
This function does not return any values. It plots the first 5 objects is the image
"""

def identify(lily_im):
  lily = lily_im<1
  lily = lily.astype(int)
  # Create a skeletonized version of the lily.
  lily_sk = skeletonize(binary_dilation(lily, selem=disk(4)))
  lily_label = label(lily_sk) # Label the objects in the skeletonized image.
  #display the labeled objects
  fig, ax = plt.subplots(ncols=5, figsize=(25,6))
  ax[0].imshow(lily_label==1)
  ax[1].imshow(lily_label==2)
  ax[2].imshow(lily_label==3)
  ax[3].imshow(lily_label==4)
  ax[4].imshow(lily_label==5)
  titles = [1,2,3,4,5]
  for i,axi in enumerate(ax):
    axi.axis('off')
    axi.set_title(titles[i])

Example
-------
#import matplotlib.pyplot as plt
#import numpy as np
#from google.colab import drive
#from skimage.morphology import label, dilation, binary_dilation, skeletonize
#from skimage.measure import regionprops, regionprops_table
#from skimage.morphology import disk, convex_hull_image
#import pandas as pd
#drive.mount('/content/drive/')

#lily_mask = plt.imread('/content/drive/MyDrive/lilymaskonly.jpg')

>>identify(lily_mask)