# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:48:55 2023

@author: rana_
"""

'''
Question 4
Create a new file called capitals.txt , store the names of five capital cities
in the file on the same line.
'''

f = open('capitals.txt','w')

f.write("London, ")
f.write("Berlin, ")
f.write("New Delhi, ")
f.write("Washington DC, ")
f.write("Moscow")

f.close()