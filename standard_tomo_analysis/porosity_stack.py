## Calculates the porosity of a binary image stack by counting black and white pixels in each slice
## -Ralph

from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import os

path = "/path/to/imag/stack/folder/"
files = os.listdir(path)
files = sorted(files)

b = 0
w = 0

for i in range(len(files)):
    name = files[i]
    name_comp = path + name
    
    im = Image.open(name_comp)
    x,y =  im.size
    
    pix = im.load()
    
    for i in range(x):
    	for ii in range(y):
    		if pix[i,ii] == 0:
    			b = b + 1
    		else:
    			w = w + 1
    w = w * 1.0
    b = b * 1.0
    print 'Porosity:' + str(b/(w + b))
    		
print 'white pixels' 
print  w
print 'black pixels'  
print  b

w = w * 1.0
b = b * 1.0

print 'Porosity'
print b/(w + b)
