#!/usr/bin/env python
# coding: utf-8

# In[8]:



def mandelbrotIter(c:complex, max_iter:int, z_abs_max:int):
    z = 0
    iteration = 0
    
    # Z_n = (Z_{n-1})^2 + c
    # Z_0 = c
    while abs(z) <= z_abs_max and iteration < max_iter:
        z = z*z + c
        iteration += 1
    return iteration/max_iter 


# In[9]:


import matplotlib.pyplot as plt
import numpy as np

# Image size (pixels)
width,height = 1800*2,1200*2



# Plot window

#" The left-most extent of the set ends with the spike at x = -2, 
# and the right side extends out to approximately x = 0.47.
#The top and bottom are at approximately y = ± 1.12"
# https://www.fractalus.com/kerry/articles/area/mandelbrot-area.html

real_start,real_end = -2,1
real_range = real_end - real_start

im_start,im_end = -1,1
im_range = im_end - im_start

#restrictive parameters
max_iter = 200
z_abs_max= 2

#initialise an n*m array (the image) 
img= np.zeros((width, height))

for x in range(0, width):
    for y in range(0, height):
        
        # pixel to complex number
        c = np.complex(real_start + (x / width) * (real_range), im_start + (y / height) * (im_range))
        
        # color scaling for the image
        img[x][y] = mandelbrotIter(c, max_iter,z_abs_max)
       
        


img = img.transpose()
plt.imshow(img, cmap="binary")
plt.axis("off")
#plt.show()
plt.savefig('mandelbrot.png')


# In[ ]:





# In[ ]:




