# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:15:36 2019

@author: Yiwei
"""
#start with a positive integer x (x is no larger than 8192 = 2**13)
x = 2019
i = 13
a = str(2**i)
b = str(x)
while x != 0:
    if x < 2**i:
        i=i-1
    else:
        output = a + "+"
        x=x-2**i
print(b + output)
