# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:12:01 2019

@author: Yiwei
"""
# read BLOUSM62 matrix
fhand=open('BLOSUM62.txt', 'r')
content=fhand.read()
lines=content.strip().split('\n')
header=lines.pop(0) # get the first column
columns=header.split() # a list containg every letter in the first column 
matrix={} # create a dictionary to store BLOSUM62 matrix
for i in lines:
    entries=i.split()
    row=entries.pop(0) # get one score once
    matrix[row]={}
    for column in columns:
        matrix[row][column]=entries.pop(0) # the score for each match is stored in the dictionary

# read three sequences
fh1=open('seq_human.txt', 'r')
seq_human=fh1.read()

fh2=open('seq_mouse.txt', 'r')
seq_mouse=fh2.read()

fh3=open('seq_random.txt', 'r')
seq_random=fh3.read()

# mouse human comparison
score=0
diff=0
diffseq=[]
seq_huamn=list(seq_human)
for i in range(len(seq_human)):
    x=matrix[seq_human[i]][seq_mouse[i]]
    score+=int(x)
    if seq_huamn[i] != seq_mouse[i]:
        diff+=1
        if int(x)<0:
            diffseq.append('*') # * represents BLOSUM score <0
        else:
            diffseq.append('+') # + represents BLOSUM score >=0
    else:
        diffseq.append(seq_human[i]) # indicate alignment with the same amino acid
        
seq_human=''.join(seq_human)  
diffseq=''.join(diffseq)
nscore=score/len(seq_human)  
identity=1-diff/len(seq_human)
print('\nSOD2_human (NP_000627.2)\n', seq_human)
print('\nSOD2_mouse (NP_038699.2)\n', seq_mouse)
print('\n'+diffseq)
print('\nBLOSUM62 score:', score) 
print('Normalized BLOSUM62 score:', nscore)
print('Identity:', '{:.2%}'.format(identity))    

# mouse random seq comparison
score=0
diff=0
diffseq=[]
seq_mouse=list(seq_mouse)
for i in range(len(seq_mouse)):
    x=matrix[seq_mouse[i]][seq_random[i]]
    score+=int(x)
    if seq_mouse[i] != seq_random[i]:
        diff+=1
        if int(x)<0:
            diffseq.append('*')
        else:
            diffseq.append('+')
    else:
        diffseq.append(seq_mouse[i])
        
seq_mouse=''.join(seq_mouse)  
diffseq=''.join(diffseq)
nscore=score/len(seq_mouse)  
identity=1-diff/len(seq_mouse)
print('\nSOD2_mouse (NP_038699.2)\n', seq_mouse)
print('\nRandomSeq\n', seq_random)
print('\n'+diffseq)
print('\nBLOSUM62 score:', score) 
print('Normalized BLOSUM62 score:', nscore)
print('Identity:', '{:.2%}'.format(identity)) 

# human random seq comparison
score=0
diff=0
diffseq=[]
seq_huamn=list(seq_human)
for i in range(len(seq_human)):
    x=matrix[seq_human[i]][seq_random[i]]
    score+=int(x)
    if seq_huamn[i] != seq_random[i]:
        diff+=1
        if int(x)<0:
            diffseq.append('*')
        else:
            diffseq.append('+')
    else:
        diffseq.append(seq_human[i])
        
seq_human=''.join(seq_human)  
diffseq=''.join(diffseq)
nscore=score/len(seq_human)  
identity=1-diff/len(seq_human)
print('\nSOD2_human (NP_038699.2)\n', seq_human)
print('\nRandomSeq\n', seq_random)
print('\n'+diffseq)
print('\nBLOSUM62 score:', score) 
print('Normalized BLOSUM62 score:', nscore)
print('Identity:', '{:.2%}'.format(identity))        