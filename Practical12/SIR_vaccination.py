# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:41:45 2019

@author: lenovo
"""
import numpy as np
import matplotlib.pyplot as plt

N = 10000 # total number of the people in the popluation
sus = []
inf = []
rec = []
list_inf=[]
inf_pro = 0.3 # infection probability
rec_pro = 0.05 # recovery probability

for i in range(0,110,10):
    vc =int(N*i/100) # an additional group of vaccinated people
    rec=[0]
    if N==vc:  # all people are vaccinated
        sus=[0]
        inf=[0] 
    else:
        sus=[N-vc-1]
        inf=[1]    
    for m in range(1,1001):
        d=np.random.choice(range(2),sus[m-1],p=[inf_pro*inf[m-1]/N,1-inf_pro*inf[m-1]/N])
        e=np.random.choice(range(2),inf[m-1],p=[rec_pro,1-rec_pro])
        ninf=np.sum(d==0) # get the number of newly infected people
        nrec=np.sum(e==0) # get the number of newly recovered people
        sus.append(sus[m-1]-ninf)
        inf.append(inf[m-1]+ninf-nrec)
        rec.append(rec[m-1]+nrec)        
    list_inf.append(inf)
# plot results
plt.figure(figsize=(6,4),dpi=150)
plt.title('SIR model with different vaccination rates')
x = range(0,1001)
# plot graphs in one figure
for u in range(0,11):
    plt.plot(x,list_inf[u],label=str(u*10)+'%') 
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.savefig("SIR_vaccination", type="png")