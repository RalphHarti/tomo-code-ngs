# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 14:46:47 2014

@author: ralph harti
"""

import Image
import os
import numpy as np
import pywt
import matplotlib.pyplot as plt

mode = 'haar'   # Defining the used wavelet
level = 2       # Defining iteration level  

path = '/path/to/input/stack/'
dir_out = '/path/to/output/stack/'

files = os.listdir(path)
files = sorted(files)

im = Image.open(path + files[1]).convert('L')
print files[1]

for i in range(len(files)):
    name = files[i]
    name_comp = path + name
    print name
    
    im = Image.open(name_comp)


    # compute coefficients of multiresolution WT
    coeffs=pywt.wavedec2(im, mode,level=level)


    # high frequency coeffs
    coeffs_H=list(coeffs)

    # discarding the low frequency
    # Approximation coeffs are from the low-pass filter
    coeffs_H[0]=np.zeros(coeffs_H[0].shape)
    # multilevel reconstruction
    imArray_H=pywt.waverec2(coeffs_H, mode)

    im_wv = Image.fromarray(imArray_H) 
    im_wv.save(dir_out + 'filename_' + str(i) + '.tif')




