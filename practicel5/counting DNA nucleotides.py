# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:05:53 2019

@author: Yiwei
"""

s="ATGCTTCAGAAAGGTCTTACG"
a=0
b=0
c=0
d=0
for char in s:
    if char == "A":
       a=a+1
    if char == "T":
       b=b+1
    if char == "C":
       c=c+1
    if char == "G":
       d=d+1

import matplotlib.pyplot as plt
labels="A", "T", "C", "G"
sizes=[a,b,c,d]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()