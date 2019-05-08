# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:12:01 2019

@author: Yiwei
"""

seq1 = 'MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
seq2 = 'MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
seq3 = 'WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'

from Bio.SubsMat import MatrixInfo
BLOSUM62 = MatrixInfo.blosum62


def compare(seqa, seqb):
    score=0 
    for i in range(0,len(seqa)):
        if (seqa[i], seqb[i]) in BLOSUM62:
            a=BLOSUM62[seqa[i],seqb[i]]
            score += a
        else:
            a=BLOSUM62[seqb[i],seqa[i]]
            score += a
    return score

print('The score for two sequences is', compare(seq1, seq2))



 