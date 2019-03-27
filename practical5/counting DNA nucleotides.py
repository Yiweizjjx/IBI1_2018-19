# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:05:53 2019

@author: Yiwei
"""
# give me a sequence of DNA
s="ATGCTTCAGAAAGGTCTTACG"
L1=list(s)
mydict = {}
for word in L1:
    if word in ["A", "T", "G", "C"]:
        if word  in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1

import matplotlib.pyplot as plt
labels = mydict.keys()
sizes= mydict.values()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()