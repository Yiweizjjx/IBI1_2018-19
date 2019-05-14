# -*- coding: utf-8 -*-
"""
Created on Mon May 13 21:42:11 2019

@author: Yiwei
"""

'''
1. find infected individuals
2. infect 8 neighbours with infection probability (0.3)
   make sure the infected person does not infect himself or infect neighbours beyond the edge
3. infected individuals may recover
   find infected individuals again
   for each infected individual, determine if it will recover with recovery probability (0.05)
4. plot the outcomes from t=0 to 100
      
'''
# import necessary libraries 
import numpy as np 
import matplotlib . pyplot as plt
# make array of all susceptible population 
population = np.zeros((100 , 100))
# start with exactly one infected person
outbreak = np.random.choice(range(100),2) 
population[outbreak[0], outbreak[1]] = 1
plt.figure(figsize =(6,4), dpi=150) 
plt.imshow(population, cmap='viridis', interpolation='nearest')
beta=0.3
gamma=0.05

for m in range(0,100):
# find infected points
  inf = np.where(population==1)
# loop through all infected points
  for i in range(0,len(inf[0])):
    # get x, y coordinates for each point
    x = inf[0][i]
    y = inf[1][i]
    # infect all 8 neighbours with probability beta
    for xNeighbour in range(x-1,x+2):
        for yNeighbour in range(y-1,y+2):
            # avoid infecting youself 
            if (xNeighbour,yNeighbour) != (x,y):
                # avoid infecting neighbours beyond the edge
                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected
                    if population[xNeighbour,yNeighbour]==0:
                        population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
  inf = np.where(population==1)
  for j in range(0,len(inf[0])):
      # infected individuals may recover with probability gamma
      a=np.random.choice(range(2),1,p=[1-gamma,gamma])[0] 
      if a==1:
          population[inf[0][j],inf[1][j]]=0.5 # the person get recovered
  plt.figure(figsize =(6,4), dpi=150) 
  plt.imshow(population, cmap='viridis', interpolation='nearest')