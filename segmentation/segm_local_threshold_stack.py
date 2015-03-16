##### This srcipt applies a local segmentation algorithm to an image stack. Useful for segmentation of images with non-uniform illumintation.
##### The OpenCV library is used for image related tasks
##### - Ralph

import cv2
import numpy as np
from matplotlib import pyplot as plt
import cv2
import numpy as np
import os


 
path = "/path/to/folder/with/image/sequence/to/be/segmented/"
files = os.listdir(path)
files = sorted(files)
#print files

for i in range(len(files)):
    name = files[i]
    name_comp = path + name
    print name
    img = cv2.imread(name_comp,0)
    
    	
    med = cv2.medianBlur(img,5)                 # Apply Median Blur
    	
    th = cv2.adaptiveThreshold(med,133,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    				cv2.THRESH_BINARY,439,-9.5)         # Local threshold with gaussian thresholding 
        
        
    kernel = np.ones((5,5),np.uint8)                            # Define kernel for morhological transformations
    th_op = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)        # opening  
    th_op_cl = cv2.morphologyEx(th_op, cv2.MORPH_CLOSE, kernel) # closing
    				
    cv2.imwrite('/path/to/result/folder/' + name, th_op_cl)
     
