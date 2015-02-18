# Aim of this program is to read a stack of binary images saved in a .vol file an image at a time and save the result as a number of .tif files in a new folder. To do that the original image is matrix multiplied with a gaussian mask. 
# Ralph  

import numpy
import scipy
from scipy import *
from numpy import *
from PIL import Image
from load_slice import load_slice
import os, sys

volfile = 'path/to/fil.vol'

##----Get the input from the vol.info file that comes with the .vol file----##
N = 690 # NUM_X from vol.info          
M = 744 # NUM_Y from vol.info 
NZ = 999 # from vol.info 
##----------##

out_dir = 'proc' # Name of the folder in which the resulting tif files should be saved

n = range(NZ)
nz = [i for i in n] # making list for slice numbers
os.mkdir( '%(n)s' %{'n':out_dir} ) # create new directory to save processed images


# Read the volume slice by slice
for ii in nz:
    a = load_slice(volfile,M,N,ii) # call load_slice

    imf = Image.fromarray(a) 
    out_file = '%(n)s/%(n)s_proc_slice%(num)s.tif' %{'n':out_dir, 'num':ii+1}
    imf.save(out_file) 




