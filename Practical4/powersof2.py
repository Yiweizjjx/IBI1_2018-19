# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:15:36 2019

@author: Yiwei
"""
# start with a positive integer x (x is no larger than 8192 = 2**13)
x = 2019
# make the first part of the sentence
y = str(x) + " is" 
# define a as string
a = str()
# loop (i can take 13,12,...,2,1)
for i in range(13,0,-1):
# find the biggest 2**i that is smaller than x
    if x >= 2**i:
# keep record
        a=a + "2**" + str(i) 
# subtract 2**i from x to find the next biggest 2**i that is smaller than x        
        x=x-2**i
# check if x is equal to 0
# if x is equal to 0, then break
# if x is not equal to 0, add " + " to link
        if x!=0:
         a=a + " + "  
# if x is equal to 1, then the last part should be "2**0"
    if x==1:
           a=a + "2**" + str(0)
# output the sentence
print(y,a) 