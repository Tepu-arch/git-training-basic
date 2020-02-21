#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math
from itertools import combinations_with_replacement


# In[2]:


ex, s = 5, 0
p = {str(i):i**ex for i in range(10)}

for cx in combinations_with_replacement('0123456789', ex+(ex>=5)):
    t = sum(p[x] for x in cx)
    sd = sum(p[x] for x in str(t))
    if t==sd and t>9: s+= t

print ("Sum of power digits for exponent", ex, "is", (s if s>0 else "*NONE*"))


# In[ ]:




