#!/usr/bin/env python
# coding: utf-8

# In[1]:


def make_great(magicians):
    great_list = []
    while magicians:
        magician = magicians.pop()
        great_list.append('the Great ' + magician)
    magicians = great_list
    return magicians
        


# In[2]:


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


# In[ ]:




