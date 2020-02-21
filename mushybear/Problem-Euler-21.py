#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
from functools import lru_cache


# In[2]:


@lru_cache(None)
def sum_div(n):
    # Taken from AJNeufeld's answer
    total = 1
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            total += x
            y = n // x
            if y > x:
                total += y
    return total

def amicable_numbers(limit):
    for a in range(limit):
        b = sum_div(a)
        if a != b and sum_div(b) == a:
            yield a

print(sum(amicable_numbers(10000)))


# In[ ]:




