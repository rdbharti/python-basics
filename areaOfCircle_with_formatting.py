# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:40:56 2023

@author: rana_
"""

# Area of Circle

pi = 3.14346345654
radius = float(input("Radius --> "))
area_circle = pi * radius**2

#print("The Circle with rdius " + "{:.2f}".format(radius) + " cm2, has area " + "{:.2f}".format(area_circle) + " cm2")

print ("radius",round(radius,2) , "area",round(area_circle,2))