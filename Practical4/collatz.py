# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:36:49 2019

@author: Yiwei
"""

#strat with a positive integer n
n = 10
while n != 1:
# if n is even, divide n by 2
# if n is odd, multiple n by 3 and add 1
 if n%2 == 0:
    n = n/2
 else:
    n = n*3 + 1
# display and run when you reach 1 for the first time
 print(n)