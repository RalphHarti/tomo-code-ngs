# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:18:51 2014

This program applies the gaussian filter, defined in removel_lf.py to a folder with images.

@author: ralph
"""
import Image
import os
import numpy as np
from remove_lf import remove_lf
from gauss_fcn2 import gauss_fcn2


dir = '/path/to/folder/with/image/stack/'

files = os.listdir(dir)
#print files


im = Image.open(dir + files[1]).convert('L')
pix = im.load()
x, y =  im.size
print x,y

stdev_x = 15
stdev_y = stdev_x

for i in files:
    print "Working on image: " + i
    im = Image.open(dir + i).convert('L')
    x, y =  im.size
    # Mask1 to remove low frequencies
    tmp_x = list(range(x)); 
    tmp_y = list(range(y));
    tmp_x[:] = [a - np.mean(range(x/2)) for a in tmp_x] # subtracting the mean of the range
    tmp_y[:] = [a - np.mean(range(y/2)) for a in tmp_y] # subtracting the mean of the range
    m1 = gauss_fcn2(stdev_x,stdev_y,tmp_x,tmp_y,0,0,1); # creating mask with other script
    m1[:] = [1 - xx for xx in m1] # subtracting the mask from 1
    
    
    m1_im = Image.fromarray(m1, 'L') 
    m1_im.save('mask.tif')
    
    b = remove_lf(im,m1) # call remove_lf
    imf = Image.fromarray(b)
    imf.save('output/path/'+i)


