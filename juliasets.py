#!/usr/bin/env python
# coding: utf-8

# In[4]:


def julia_iter(z:complex,c:complex,z_abs_max:int, max_iter:int):
    
    iteration = 0
    rat= 0
    
    while abs(z) <= z_abs_max and iteration < max_iter:
        z = z**2 + c
        iteration += 1
    if(iteration / max_iter > 0.8):
        rat = 1
    return iteration / max_iter


# In[7]:


import numpy as np
import matplotlib.pyplot as plt
#import gc
#gc.collect()

# Image size (pixels)
width, height = 900, 900

# Plot window
xmin, xmax = -1.5, 1.5
xrange = xmax - xmin
ymin, ymax = -1.5, 1.5
yrange = ymax - ymin

#restrictive parameters
z_abs_max = 8 #3
max_iter = 60 #20

#initialise an n*m array (the image)
julia_img= np.zeros((width, height))

#complex number c
c= np.complex(-2,0) #denditric fractal
#c= np.complex(-0.39,-0.59) # Siegel Disk Fractal
#c= np.complex(-0.123,0.745) #Douady's Rabbit Fractal
#c= np.complex( -0.25,0) #topologically equivalent to a circle
#c= np.complex(0.27334,0.00742)
#c = np.complex(-0.77967939051932,0.11124251677182495)

for ix in range(width):
        for iy in range(height):
            
            # pixel to complex number
            z = np.complex(ix / width * xrange + xmin, iy / height * yrange + ymin)
            
            # color scaling for the image
            julia_img[ix, iy] = julia_iter(z,c,z_abs_max, max_iter)
           
            

plt.imshow(julia_img, cmap="binary")
plt.axis("off")

plt.show()
plt.savefig('juliasets.png')


# In[ ]:




