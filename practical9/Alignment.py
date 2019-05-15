# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:12:01 2019

@author: Yiwei
"""
# read BLOUSM62 matrix
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

# read three sequences
fh1=open('seq_human.txt', 'r')
seq_human=fh1.read()

fh2=open('seq_mouse.txt', 'r')
seq_mouse=fh2.read()

fh3=open('seq_random.txt', 'r')
seq_random=fh3.read()

