# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:22:42 2023

@author: rana_
"""
import random
c = 0
my_list = []
while (c<20):
    rand_num = random.randint(100, 999)
    my_list.append(rand_num)
    c += 1

print(my_list)
    
xx = my_list
xx.sort()
print (xx)