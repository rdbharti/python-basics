# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:12:48 2023

@author: rana_
"""

version_num = input("Enter Version number: ")
major, minor, patch = version_num.split(".")
print ("major =",major, "\nminor = ",minor, "\npatch = ", patch)


while True:
    print("1. Major")
    print("2. Minor")
    print("3. Patch")
    
    change = int(input("Enter the option: "))
    
    if change == 1:
        major = input("Enter Major Version Number")
        break
    if change == 2:
        minor = input("Enter Minor Version Number")
        break
    if change == 3:
        patch = input("Enter Minor Version Number")
        break
new_version = major+"."+minor+"."+patch

print("New Version is: ", new_version)