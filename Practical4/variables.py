# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:15:22 2019

@author: Yiwei
"""

a = 234
b = 234234
print(b%7)
c = b/7
d = c/11
e = d/13
print(a < e)
print(a == e)
print(a > e)


X = True
Y = True
Z = (X and not Y) or (Y and not X)
W = X != Y
print(Z)
print(W)