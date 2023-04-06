# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:03:18 2023

@author: rana_
"""

'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''

def copy_file(file1, file2):
    with open(file1, 'r') as fromFile:
        with open(file2, 'w') as toFile:
            toFile.write(fromFile.read())
            
copy_file('capitals.txt', 'capitals2.txt')