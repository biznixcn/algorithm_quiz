#!/usr/bin/python
#-*-coding:utf-8-*-

"""
    You are given a set of numbers 0‐n.  Given a k, print all subsets of size k. 

    r-组合算法
"""


import random
from pprint import pprint 
#import pdb; pdb.set_trace()

n = 8
setnums = range(0,n)
k = random.randint(1,n)
startseq = range(0,k)
endseq = range(n - k,n)
result = []
result.append(startseq)

def findsubset(pre=[]):
    for i,j in enumerate(pre[::-1],1):
        if j < n - 1 and (j + 1) not in pre:
            break
    temp = [pre[m] for m in xrange(k - i)]
    temp.extend([j + m for m in xrange(1,k - len(temp) + 1)])
    if temp == endseq:
        return 
    result.append(temp)
    findsubset(temp)

findsubset(startseq)
result.append(endseq)

print "original sets: ",setnums
print "k value: ",k
print "result: "
pprint(result)
print "the length of result is: ",len(result)
