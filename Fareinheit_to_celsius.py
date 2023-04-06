# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:54:10 2023

@author: rana_
"""

#C = [(F-32)×5]/9

far = float(input("Temperature in Farenheit: "))
cel = (far-32)*5 / 9
print("{:.2f}".format(far) + " degree farenheit is equals to " + "{:.2f}".format(cel) + " degree Celcius.")