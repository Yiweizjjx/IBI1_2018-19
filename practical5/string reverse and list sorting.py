# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:51:42 2019

@author: Yiwei
"""
# give me a string of words
s = "but soft what light in yonder window breaks"
# split the string
L1 = s.split(" ")
# create an empty list L2 
L2 = []
# loop (for every element in L1)
for i in L1:
# reverse every element in L1 and add them to L2
    L2.append(i[::-1])
# sort the elements of L2 in place
L2.sort()
# reverse the elements of L2 in place
L2.reverse()
print(L2)