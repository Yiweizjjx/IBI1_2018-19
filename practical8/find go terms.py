# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:04:54 2019

@author: Yiwei
"""

from xml.dom.minidom import parse  
import xml.dom.minidom
import re

DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement 
defstr = collection.getElementsByTagName("defstr")
i=0
L1=[]
L2=[]
for i in range(0,len(defstr)):
   a=defstr.item(i)
   b=a.childNodes[0].data
   if re.search(r'autophagosome+', b):
      L1.append(b)
      id_1=a.parentNode.parentNode.parentNode.getElementsByTagName('id')
      id_value = id_1.childNodes[0].data
      L2.append(id_value)
   i = i+1
print(L1)
print(L2)