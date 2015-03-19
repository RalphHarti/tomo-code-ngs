# This script can read in .vol images of 'filename' one slice at a time and return each slice as an array.
# @author: ralph harti (tpnspign@gmail.com)

from scipy import *
from numpy import *
import numpy
import scipy
import array
from PIL import Image
import Image, numpy
import struct



def load_slice ( filename,M,N,Z ):
    #M = N
    
    fid = open(filename, 'rb')

    res = []

    fid.seek((M*N*Z*4),0)
    
    data = numpy.fromfile(fid,'float32',N*M)
    
    fid.close()
    
   
    res = numpy.reshape(data,(M,N))
    
    return res

