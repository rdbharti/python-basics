# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:22:05 2023

@author: rana_
"""

'''
Question 3
Create a LinkedList to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

dataType = ['Open', 'High', 'Low', 'Close']
dataValue = [[12.87, 13.23, 11.42, 13.10], [23.54,25.76,21.87,22.33], [98.99,102.34,97.21,100.065], [203.63,207.54,202.43,205.24]]
Companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']

combineData = {}
    
# for i in range(0, len(dataValue)):
#     print()
#     print(Companies[i], end='\n')
#     for j in range(0, len(dataValue[i])):
#         print(f"{dataType[j]} -- {dataValue[i][j]}")
#         combineData[Companies[i]] = {dataType[j]:dataValue[i,j]}
        
# print(combineData)

for i in range(0, len(dataType)):
    combineData[Companies[i]] = dict(zip(dataType,dataValue[i]))
    
print(combineData)