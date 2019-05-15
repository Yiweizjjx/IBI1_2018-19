# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:12:01 2019

@author: Yiwei
"""
fhand=open('BLOUSM62.txt', 'r')
content=fhand.read()
lines=content.strip().split('\n')
header=lines.pop(0)
columns=header.split()
matrix={}
for i in lines:
    entries=i.split()
    row=entries.pop(0)
    matrix[row]={}
    for column in columns:
        matrix[row][column]=entries.pop(0)
