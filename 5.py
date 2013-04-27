#!/usr/bin/python
#-*-coding:utf-8-*-

"""
    Find n-­‐th largest item in an incoming array.

    the variant of the quicksort.
"""


import random
#import pdb; pdb.set_trace()

nums = range(1,10)
random.shuffle(nums)
k = random.randint(1,9)

def select_k_max(l=[],k = k):
    if len(l) == 1:
        return l[0]
    else:
        pre = [i for i in l[1:] if i < l[0]]
        last = [i for i in l[1:] if i >= l[0]]
        if len(last) == k - 1:
            return l[0]
        elif len(last) < k - 1:
            return select_k_max(pre,k - len(last) - 1)
        else:
            return select_k_max(last,k)

print "the random sets is: ",nums
print "get the %s largest num"%k
print "the result is: ",select_k_max(nums,k)
