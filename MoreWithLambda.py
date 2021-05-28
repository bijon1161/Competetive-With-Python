# -*- coding: utf-8 -*-
"""
Created on Fri May 28 20:21:17 2021

@author: Admin
"""

num1 = [1,2,3]
num2 = [5,5,5]
print(list(map(lambda x,y:x**y,num2,num1)))