# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:03:19 2023

@author: rana_
"""

'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''

# fibo = {'name':'rana'}
# fibo['age']=30

fibo = []
indexed_fibo = {}

# fibonacchi
a = 0
b = 1
sum = 0 
count = 2

fibo.append(a)
fibo.append(b)

while (count < 12) and (count > 0):
    sum = a+b
    a,b = b,sum
    fibo.append(sum)
    count += 1


# Initialise index

for i in range(1, 13):
    indexed_fibo[str(i)] = str(fibo[i-1])
    
print(indexed_fibo)