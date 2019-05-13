# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:12:45 2019

@author: Yiwei
"""
# import necessary libraries 
import numpy as np 
import matplotlib . pyplot as plt

# initial values of each of the popluation
a=9999 # susceptible people
b=1 # infected people
c=0 # recovered people
N=10000 # total number of the people in the popluation
inf_pro=0.3 # infection probability
rec_pro=0.05 # recovery probability

# create arrays to track how variables evolve over time
sus=np.array([a])
inf=np.array([b])
rec=np.array([c])
for m in range(1,1001):
    d=np.random.choice(range(2),a,p=[inf_pro*a/N,1-inf_pro*a/N])
    e=np.random.choice(range(2),b,p=[rec_pro,1-rec_pro])
# get the number of newly infected people
    ninf=np.sum(d==0)
# get the number of recovered people
    nrec=np.sum(e==0)
    a-=ninf
    b=b+ninf-nrec
    c+=nrec
# record the output
    sus=np.append(sus,a)
    inf=np.append(inf,b)
    rec=np.append(rec,c)

# plot results
plt.figure ( figsize =(6 ,4) , dpi=150)
plt.title('SIR model')
plt.plot(sus, label='susceptible')
plt.plot(inf, label='infected')
plt.plot(rec,  label='recovered')
plt.legend() 
plt.xlabel('time')
plt.ylabel('number of people')
plt.show()
plt.savefig("SIR", type="png")
