# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:15:22 2019

@author: lenovo
"""

a = 233
b = 233233
print(b%7)
c = b/7
d = c/11
e = d/13

X = True
Y = True
Z = (X and not Y) or (Y and not X)
W = X != Y
print(Z)
print(W)