#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from cmath import sqrt

dist = lambda x1,y1,x2,y2 : abs(sqrt((x2 - x1)**2 + (y2 - y1)**2))

max_depth = 1000000
#c = np.complex(-0.77967939051932,0.11124251677182495)
c= np.complex(0,0)
stack = []
depth  = 0
points= []
res=0.01

#inv f(z)= g(z)= +- sqrt(z-c)
stack.append(np.complex(1,0))

depth += 1

while(len(stack) != 0):
    current = stack.pop()
    
    c1 = sqrt(current-c)
    c2 = -c1
    
    point_in_range, i = 0,0
    
    #point_in_range = 0 means no points within range
    #point_in_range = 1 means c1 within range only
    #point_in_range = 2 means c2 within range only
    #point_in_range = 3 means c1 and c2 within range 
    
    while(i < len(points) and point_in_range != 3):
        dist1= dist(c1.real,c1.imag,points[i][0],points[i][1])
        dist2= dist(c2.real,c2.imag,points[i][0],points[i][1])
        
        if (dist1 < res and point_in_range == 0):
            point_in_range = 1
        if(dist2 < res and point_in_range == 0):
            point_in_range = 2
        if(dist2 < res and point_in_range == 1) or (dist1 < res and point_in_range == 2):
            point_in_range = 3 
            
        i += 1 
    
    #if _ point not within range (c_n-res, c-n+res) append to list of points 
    if(point_in_range == 0 or point_in_range == 2):
        points.append((c1.real,c1.imag))
        
    if(point_in_range == 0 or point_in_range == 1):
        points.append((c2.real,c2.imag))
    
    if(depth > max_depth): 
        current = stack.pop() 
        depth -= 1
        
    else:
        stack.append(c1)
        stack.append(c2)
        depth += 1
        
xs, ys = [], []

for x, y in points:
    xs.append(x)
    ys.append(y)
    
plt.scatter(xs,ys,s= 0.5,color="black")
#plt.show()
plt.axis("off")
plt.savefig('inverseIteration.png')


# In[ ]:




