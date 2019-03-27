# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:01:57 2019

@author: Yiwei
"""
import re
fhand = open('address_information.csv', 'r')
x = str() 
L1 = []
name_list = []
address_list = []
subject_list = []
for a in fhand:
    mylist = re.split(r',', str(a))
    if re.search(r'@', mylist[1]) == None:
       continue
    if re.match(r'.com', mylist[1]):
         print(mylist[1], ':Correct Address!')
         name_list = name_list + [mylist[0]]
         address_list += [mylist[1]]
         subject_list += [mylist[2]]
    else:
         print(mylist[1], ':Wrong Address!')
