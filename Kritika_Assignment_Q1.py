#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
stardata = pd.read_csv("stardata.csv", header = None)
#stardata
stardata2=stardata.dropna()
#print(stardata2)
RA = stardata.loc[:,0]
#print(RA)
Dec = stardata.loc[:,1]
#print(Dec)
Parallax = stardata2.loc[:,2]
#print(Parallax)
App_magn = stardata.loc[:,3]
#print(App_magn)
Distance = 1000/Parallax
#print(Distance)
Abs_magn = App_magn+5-(5*np.log10(Distance))
print(Abs_magn)


# In[12]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
stardata = pd.read_csv("stardata.csv", header = None)
stardata2=stardata.dropna()
RA = stardata.loc[:,0]
Dec = stardata.loc[:,1]
Parallax = stardata2.loc[:,2]
App_magn = stardata.loc[:,3]
Distance = 1000/Parallax
Abs_magn = App_magn+5-(5*np.log10(Distance))
plt.hist(Abs_magn,bins=50,edgecolor='black',color='red')
plt.title('Histogram')
plt.xlabel('Absolute Magnitude')
plt.ylabel('Numerical Value')


# In[8]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
stardata = pd.read_csv("stardata.csv", header = None)
stardata2=stardata.dropna()
App_magn = stardata.loc[:,3]
RA = stardata.loc[:,0]
Dec = stardata.loc[:,1]
plt.scatter(RA,Dec,s=15-App_magn)
plt.title('Scatterplot')
plt.xlabel('Right Ascension')
plt.ylabel('Declination')


# In[ ]:




