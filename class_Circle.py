# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 23:08:45 2023

@author: rana_
"""

'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''

class Circle(object):
    ''' This will take in radius and print out area '''
    
    def __init__(self, r=0.0):
        self.radius = r
    
    def area(self):
        area = 3.14 * (self.radius)**2
        return area
    

cir = Circle(10.0)
print(cir.area())
    
        
        