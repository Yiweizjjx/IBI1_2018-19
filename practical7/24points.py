# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:08:42 2019

@author: Yiwei
"""


import re
from operator import mul, sub, add
 
 
def div(a, b):
    if b == 0:
        return 999999.0
    return a / b
 
ops = {mul: '*', div: '/', sub: '-', add: '+'}
 
def solve24(num, how, target):
    if len(num) == 1:
        int(num)
        if round(num[0], 5) == round(target, 5):
            yield str(how[0]).replace(',', '').replace("'", '')
    else:
        for i, n1 in enumerate(num):
            for j, n2 in enumerate(num):
                if i != j:
                    for op in ops:
                        new_num = [n for k, n in enumerate(num) if k != i and k != j] + [op(n1, n2)]
                        new_how = [h for k, h in enumerate(how) if k != i and k != j] + [(how[i], ops[op], how[j])]
                        yield from solve24(new_num, new_how, target)
 
# input numbers
str_number=input("Please input numbers to computer 24:(use ',' to divide them)" )
L1=re.split(r',',str_number)
print(L1)
for nums in L1:
    print(nums, end=' : ')
    try:
        print(next(solve24(nums, nums, 24)))
    except StopIteration:
        print("No solution found")