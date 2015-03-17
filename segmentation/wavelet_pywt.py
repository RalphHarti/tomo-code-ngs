# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 14:46:47 2014

@author: ralph
"""

import Image
import numpy as np
import pywt
import matplotlib.pyplot as plt

mode = 'haar'   # Defining the used wavelet
level = 2       # Defining iteration level  

path = '/media/ralph/932C-E76A/image_dump/'

#files = os.listdir(dir)
#print files
im = Image.open(path + 'Kim_test.tif')
#im = Image.open(dir + files[1]).convert('L')
#print files[1]

#im = Image.open('/media/ralph/932C-E76A/Dropbox/studium/spyder_workspace_studium/wavelets/lena.png')
# compute coefficients of multiresolution WT
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
