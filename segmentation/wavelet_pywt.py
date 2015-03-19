# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 14:46:47 2014

This program computes the wavelet part of the segmentation procedure presented in "3D Imaging of Porous Rocks 
Length Scales and Fluid Distribution" by Ralph P. Harti (Master Thesis).
Only for a single image - to treat an image stack see other script.

@author: ralph harti (tpnspign@gmail.com)
"""

import Image
import numpy as np
import pywt
import matplotlib.pyplot as plt

mode = 'haar'   # Defining the used wavelet
level = 2       # Defining iteration level  

path = '/path/to/folder/with/image/'

im = Image.open(path + 'filename.tif')

coeffs=pywt.wavedec2(im, mode,level=level)


# high frequency coeffs
coeffs_H=list(coeffs)
#print coeffs_H[0]

# discarding the low frequency
# Approximation coeffs are from the low-pass filter
coeffs_H[0]=np.zeros(coeffs_H[0].shape)
# multilevel reconstruction
imArray_H=pywt.waverec2(coeffs_H, mode)

im_wv = Image.fromarray(imArray_H) 
im_wv.save('out.tif')


im.save('org.tif')

wavelet = pywt.Wavelet(mode)
phi, psi, x = wavelet.wavefun(level=level)

plt.plot(x,psi)
plt.show()
