## This code was provided by H. O. Sørensen (University of Copenhagen)

"""
The marching cube algorithm is used to calculated the specific surface area of a binary image stack of a porous 
system. The dictionary in the file "Surface_area.py" is used for evaluation.


"""
#from scipy import ndimage
import numpy as np
import fabio
#from Surface_area import MC_Surface
from Surface_area import MC_Surface
import time


t0 = time.time()
## User Input

ncpus = 16 # number of cpu kernels
firstImage = 100
lastImage = 185

dir = '/path/to/folder/with/images/'
# Choose subvolume for evalution (if numbers are None the full volume is used)
x1 = None
x2 = None 
y1 = None
y2 = None 
#x1 = 0
#x2 = 500 
#y1 = 0
#y2 = 500 


dim1, dim2 = fabio.open('%sfilename%d.tif' %(dir,firstImage)).data.shape #determine x,y size of volume
if x1 == None: x1= 0
if x2 == None: x2= dim1
if y1 == None: y1= 0
if y2 == None: y2= dim2

no_slices = lastImage - firstImage
vol = np.zeros((no_slices,dim1,dim2),dtype=np.bool)


slice = 0
for i in range(firstImage,lastImage):
    vol[slice] = fabio.open('%sfilename%d.tif' %(dir,i)).data.astype(np.bool)
    slice +=1

#vol[vol==255] = 1
print 'Succesfully read volume'


AOI = vol[:,x1:x2,y1:y2] # Here is the volume reduced to 500 by 500

#         (Surf_area[pixel_area] * pixel_area[mu**2])           cm**3       10**-6 m**3      m**2
# BET =   -------------------------------------------  =     [  ------ ] =  ------------ = -------
#          Nvoxel * Vvox [mu**3] * rho_mater [g/cm**3]           mu * g       10**-6 m g       g

#                     Surf_area[pixel_area]
#      =  -------------------------------------------
#          Nvoxel * pix_length [mu] * rho_mater [g/cm**3]

Nvoxel = (AOI == 1).sum() # Number of material (rock) voxels
rho_mater = 2.71 # Density of the rock - here it is for Dolomite (CaMg(CO3)2), Calcite is 2.71  
len_voxel = 0.02 # Length of voxel in micrometers
porosity = 1.0 * Nvoxel/len(AOI.ravel()) 
porosity = 1 - porosity 


### Parallel part
import time
t1 = time.clock()

import pp
job_server = pp.Server(secret='test')
parts = ncpus
jobs=[]
job_server.set_ncpus(ncpus)

print "Starting ", job_server.get_ncpus(), " workers"

# submit sub jobs
step = AOI.shape[0]/parts
for section in range(parts):
        if section < parts-1:
            AOI_sub = AOI[section*step:(section+1)*step+1,:]
        else:   
            AOI_sub = AOI[section*step:(section+1)*step,:]
        jobs.append(job_server.submit(MC_Surface, (AOI_sub,)))


Surf_area_parts = [job() for job in jobs]
print 'Done - area calculation in %f sec' %(time.clock()-t1)
Surf_area = np.array(Surf_area_parts).sum()
BET_area = Surf_area/(Nvoxel*len_voxel*rho_mater)
print 'BET area (m^2/g): ', BET_area

#Calculate Kozeny-Carman permeability
C = 1./6
print rho_mater
Permeability_KozenyCarman = C* (porosity**3 / (BET_area*rho_mater*(1-porosity))**2) *10**3
print 'Kozeny-Carman permeability (mD):', Permeability_KozenyCarman
print 'Porosity: ', porosity

t2 = time.time()
total_time = t2-t0

print 'Time to calculate all the values in sec: %f' %(total_time) 



