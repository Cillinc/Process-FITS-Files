# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:30:38 2020

@author: - Cillin O Foghlu
Student ID 18186751
"""

#import numpy as np
#import pandas as pd
#from array import *
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
import glob, os
os.chdir('d:\\project\\masters\\fits\\stars')
#import cv2

# open input file to process it line by line.
# each line is the name of a fits compressed file
# after taking in the file name the end of line ( "\n" ) character must be removed

i = 0

for file in glob.glob("**/*.fits.bz2", recursive = True):
    fits_file = fits.open(file, memmap=True)
    image = fits_file[0].data
      
#   plot the image and then save it with the new naming format
#   close plots once saved to conserve memory

    plt.figure()
    plt.imshow(image, cmap='gray', vmin=0, vmax=0)
    plt.colorbar()
    # remore the "'fits.bz2 " from file names
    file = file[:-9]
    # add an "s" to the file to signify that the image file is for a star
    plt.savefig("s" + file + ".png")
    plt.close()
    i= i+1
    # tracker to show progress
    print(i)
    print(file)
        