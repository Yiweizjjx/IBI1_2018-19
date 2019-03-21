# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:51:42 2019

@author: Yiwei
"""

s = "but soft what light in yonder window breaks"
L1 = s.split(" ")
L2 = L1.copy()
L3 = []
for i in L2:
    L1.remove(i)
    i = i[::-1]
    L3.append(i)
L3.sort()
L3.reverse()
print(L3)