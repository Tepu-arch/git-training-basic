#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math
from math import factorial as fact


# In[2]:


fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
sfd = lambda n: sum(fact[int(i)] for i in str(n))
print (sum(i for i in range(10, int(input("N?"))) if sfd(i)%i == 0))


# In[3]:


print (sum(i for i in range(10, int(input("N?"))) if sfd(i)%i == 0))


# In[ ]:




