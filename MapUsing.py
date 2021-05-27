# -*- coding: utf-8 -*-
"""
Created on Thu May 27 19:49:16 2021

@author: Admin
"""
numbers=[1,2,3,4]
def square(number):
    number = number**2
    return number
print(list(map(square,numbers)))