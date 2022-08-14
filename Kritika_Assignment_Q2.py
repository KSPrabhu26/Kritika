#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics
from scipy.optimize import curve_fit as cf
Hdata = pd.read_csv("data.txt")
#Hdata
dist_mod=Hdata.loc[:,'mod0']
#dist_mod
vel=Hdata.loc[:,'vgsr']
#print(vel)
x = dist_mod/5-5
Distance = 10**x
#print(Distance)
plt.scatter(Distance,vel,s=5)
plt.xlabel('Distance(Mpc)')
plt.ylabel('Recession velocity(km/s)')
plt.title("Hubble's Constant")
#plt.xscale('log')
#plt.yscale('log')
def lin_func(x,m,c):
    return m*x + c
p_opt,p_cov = cf(lin_func,Distance,vel)
plt.plot(Distance,lin_func(Distance,*p_opt),label='Best Fit', color = 'black')
H0=p_opt[0]
age=1000/H0
print(f"The age of the universe is {age}")


# In[ ]:




