# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:17:39 2014

@author: ralph
"""

# This script applies a gaussian mask to a fourier shifted image in order to remove low frequency
# artefacts.
# Ralph Harti

import numpy
import scipy
from scipy import *
from numpy import *
from gauss_fcn2 import gauss_fcn2

def remove_lf( imIn,m1 ):
    imf = numpy.fft.fft2(imIn);
    imf = numpy.fft.fftshift(imf);
    
    imf = numpy.multiply(m1,imf);# convolute shifted fourier with mask
    imf = numpy.fft.fftshift(imf);
    
    b = real(fft.ifft2(imf)); # get only the real part of the inverted fourier of imf
    imOut = numpy.array(b); # getting an array of results, just for python reason
    return imOut