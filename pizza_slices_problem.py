# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 21:59:28 2023

@author: rana_
"""

total_people = int(input("Total Number of people --> "))
total_slices_neede = total_people*4

total_pizzas = 0

while True:
    total_pizzas = total_pizzas+1
    slices = total_pizzas*6
    if (slices >= total_slices_neede):
        print("Minimum pizzas required is ", total_pizzas)
        print("Slices remaining will be", slices-total_slices_neede)
        break;