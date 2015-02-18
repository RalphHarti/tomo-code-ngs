# Aim of this program is to read a stack of binary images saved in a .vol file an image at a time, process it with remove_lf to remove low frequency artefacts and save the result as a number of .tif files in a new folder. To do that the original image is matrix multiplied with a gaussian mask. 
# Ralph  

import numpy
import scipy
from scipy import *
from numpy import *
from PIL import Image
#from remove_lf import remove_lf
#from gauss_fcn2 import gauss_fcn2
from load_slice import load_slice
import os, sys

volfile = 'p3-1.1.3 clean-unclean 2.vol'
 
# '/media/bohr/bohr_storage/CT_data_DTU/CT_data_DTU/p3-1.1.1 clean [2014-09-25 10.29.37]/'

#volfile = '/home/CT_data_DTU/p3-1.1.1 clean [2014-09-25 10.29.37]/p3-1.1.1 clean_07/p3-1.1.1 clean.vol'

#volfile = '/media/ralph/932C-E76A/Dropbox/NanoGeoScience_project/volfile_process/volfile/XXXI_premount_25nm_pos2_rec_nopf_0001.vol' 

N = 690 #1000 #2048 # NUM_X from vol.info -> 2048          690 744 999
M = 744  #1000 #2048 # NUM_Y from vol.info -> 2048 
NZ = 999 #1000 #255 # from vol.info -> 256
name_1 = 'proc' # Name of the folder in which the resulting tif files should be saved

n = range(NZ)
nz = [i for i in n] # making list for slice numbers
os.mkdir( '%(n)s' %{'n':name_1} ) # create new directory to save processed images


# Read the volume slice by slice
for ii in nz:
    a = load_slice(volfile,M,N,ii) # call load_slice

    imf = Image.fromarray(a) 
    #name_2 = '%(n)s_proc_lf/%(n)s_proc_slice%(num)s.tif' %{'n':name_1, 'num':ii+1}
    name_2 = '%(n)s/%(n)s_proc_slice%(num)s.tif' %{'n':name_1, 'num':ii+1}
    imf.save(name_2) 
 




