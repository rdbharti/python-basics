# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 22:54:07 2023

@author: rana_
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''

class Bank(object):
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, withdraw):
        if (withdraw > self.balance):
            print(f"Insufficient Balance {self.balance}")
        else:
            self.balance = self.balance-withdraw
            print(f"Amount Withdrawn = {withdraw}\nBalance = {self.balance}")
    
    def display_balance(self):
        print(f"The Balance is {self.balance}")
        
    def deposite(self, deposit):
        self.balance = self.balance+deposit
        print(f"Amount Deposited = {deposit}\nBalance = {self.balance}")
    

x = Bank(10000)
x.display_balance()
x.withdraw(4500)

x.deposite(45896)

    