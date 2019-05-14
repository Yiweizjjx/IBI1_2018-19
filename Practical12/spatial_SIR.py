# -*- coding: utf-8 -*-
"""
Created on Mon May 13 21:42:11 2019

@author: Yiwei
"""
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

for m in range(0,20):
# find infected points
  inf = np.where(population==1)
# loop through all infected points
  for i in range(len(inf[0])):
    # get x, y coordinates for each point
    x = inf[0][i]
    y = inf[1][i]
    # infect each neighbour with probability beta
    # infect all 8 neighbours (this is a bit finicky, is there a better way?):
    for xNeighbour in range(x-1,x+2):
        for yNeighbour in range(y-1,y+2):
            # don't infect yourself! (Is this strictly necessary?)
            if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                    if population[xNeighbour,yNeighbour]==0:
                        population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    inf = np.where(population==1)
    for j in range(0,len(inf[0])):
        a=np.random.choice(range(2),1,p=[1-gamma,gamma])[0]
    if a==1:
        population[inf[0][j],inf[1][j]]=0.5
  plt.figure(figsize =(6,4), dpi=150) 
  plt.imshow(population, cmap='viridis', interpolation='nearest')