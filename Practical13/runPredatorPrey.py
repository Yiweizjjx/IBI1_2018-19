# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:08:34 2019

@author: Yiwei
"""
# run a Copasi ﬁle from within Python
import os
import numpy as np
import matplotlib . pyplot as plt
import xml.dom.minidom

os.chdir('D:/IBI1/practical/IBI1_2018-19/Practical13') 

def xml_to_cps():
    import os
    import xml.dom.minidom
    
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
        
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()

xml_to_cps()
os.system("CopasiSE.exe predator−prey.cps")

# alter the SBML ﬁle
pm={} # create a dictionary to store the four parameters
DOMTree = xml.dom.minidom.parse("predator-prey.xml")
collection = DOMTree.documentElement 
para = collection.getElementsByTagName('parameter')
for i in range(0,4):
    num = np.random.sample()
    pm_name = para[i].getAttribute('id')
    pm[pm_name]=num
    para[i].setAttribute('value',str(num))
filexml = open('predator-prey.xml','w')
DOMTree.writexml(filexml)
filexml.close()

# read and plot simulation results
data=open('modelResults.csv', 'r')
count=0
results=[[],[],[]]
for line in data:
    line=line.rstrip()
    count+=1
    if count==1:
        variable=line.split(',')
        names=np.array([variable])
    else:
        result=line.split(',')
        results[0].append(result[0])
        results[1].append(result[1])
        results[2].append(result[2])
        
results = np.array(results) # transform it into a numpy array
results = results.astype(np.float) # transform the numbers into actual numbers 
# plot a time course of the predator and prey population
plt.title('Time course')
plt.plot(results[0],results[1],label='Predator (b=' + str(pm['k_predator_breeds']) + ', d=' + str(pm['k_predator_dies']) + ')')
plt.plot(results[0],results[2],label='Prey (b=' + str(pm['k_prey_breeds']) + ', d=' + str(pm['k_prey_dies']) + ')')
plt.xlabel('time')
plt.ylabel('population')
plt.legend()
plt.show()
#  plot predator population against prey population
plt.title('Limit cycle')
plt.plot(results[2],results[1])
plt.xlabel('predator popluation')
plt.ylabel('prey popluation')
plt.show()

# asses the results
'''
1. run 100 simulations with 100 diﬀerent parameter combinations
2. record the number of predators and prey
3. plot the outcomes in one figure  
'''