# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:08:42 2019

@author: Yiwei
"""
import re
from fractions import Fraction
# The input numbers must be interger between 1 and 23
re_numtest = re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-3]$)') # 1-9, 10-19, 20-23
i = 1
while i: # if i is not equal to 0,then loop
    i = 0
    data = input('Please input numbers to computer 24:(use \',\' to divide them)\n')
    numList = data.split(',')
    for char in numList:
        if re_numtest.match(char): 
            continue
        else: 
            print('The input number must be intergers from 1 to 23')
            i = 1
            break

num = list(map(int,numList)) # map:change every element into integer
# recursion times
count = 0 

# n is len(num) 
def dfs(n):
    global count
    count = count +1
    
    if n == 1:
        if(float(num[0])==24):
            return 1 
        else:
            return 0 
    
    # select two different numbers
    for i in range(0,n):
        for j in range(i+1,n):
            a = num[i]
            b = num[j]
            num[j] = num[n-1]
            # merging them all available operands 
            num[i] = a+b
            if(dfs(n-1)):
                return 1
            
            num[i] = a-b
            if(dfs(n-1)):
                return 1  
            
            num[i] = b-a
            if(dfs(n-1)): 
                return 1                                                                     
            
            num[i] = a*b
            if(dfs(n-1)): 
                return 1  
            
            if a:
                # floats are not precise
                num[i] = Fraction(b,a)
                if(dfs(n-1)): 
                    return 1 
                
            if b:
                num[i] = Fraction(a,b)
                if(dfs(n-1)): 
                    return 1 
            # Backtracking  
            num[i] = a
            num[j] = b
    return 0 # found a 24 point solution

if (dfs(len(num))): 
    print('Yes')
else: 
    print('No')
print('Recursion times:',count)