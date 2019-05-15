# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:04:54 2019

@author: Yiwei
"""

import xml.dom.minidom
import re
import pandas as pd
'''
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
'''
###
def Child(id, resultSet):
    for t in go:
        parents = t.getElementsByTagName('is_a')
# parents is a list of elements        
        geneid = t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultSet.add(geneid)
                Child(geneid,resultSet)
# create a pandas.Dataframe to store the output               
df = pd.DataFrame(columns=['id','name','definition','childnodes'])

#create the DOM tree
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement 
go = collection.getElementsByTagName("term")
for term in go:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    # find terms that contain the word 'autophagosome'
    if re.search(r'autophagosome+', defstr):
        id = term.getElementsByTagName('id')[0].childNodes[0].data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
        resultSet = set()
        # Use set! once the item  was found,it can only be counted once
        # reduce redundancy
        Child(id, resultSet)
        df = df.append(pd.DataFrame({'id':[id], 'name':[name], 'definition':[defstr], 'childnodes':[len(resultSet)]}))
        print(id, len(resultSet))

fname='autophagosome.xlsx'
df.to_excel(fname, index=False)