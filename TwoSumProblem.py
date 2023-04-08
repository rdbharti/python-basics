#!/usr/bin/env python
# coding: utf-8

# In[19]:


nums = [3,3]
sum = 6


# In[20]:


def two_sum(n, target):
    out = list()
    for i in range(len(n)):
        req = target-n[i]
        for j in range(i+1,len(n)):
            if (n[j] == req):
                out.append(i)
                out.append(j)
    return out
        


# In[21]:


print(two_sum(nums,sum))


# In[ ]:




