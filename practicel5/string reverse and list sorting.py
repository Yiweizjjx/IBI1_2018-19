# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:51:42 2019

@author: Yiwei
"""

s = "but soft what light in yonder window breaks"
L1 = s.split(" ")
L2 = L1.copy()
L3 = []
i = []
i = L2(0)
for i in L2:
    i.reverse()
    L3.append(i)
    L2.remove(i)
    i = L2(0)
L4 = L3.sort()
L5 = L4.reverse()
print(L5)