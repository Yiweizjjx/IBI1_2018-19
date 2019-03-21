# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:51:42 2019

@author: Yiwei
"""

s = "but soft what light in yonder window breaks"
L1 = s.split(" ")
L2 = []
for i in L1:
    L2.append(i[::-1])
L2.sort()
L2.reverse()
print(L2)