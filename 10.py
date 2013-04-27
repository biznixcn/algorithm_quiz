#!/usr/bin/python
#-*-coding:utf-8-*-

"""
    写一个算法，从n个数的序列中找出最长的单调递增子序列，并分析算法的时间复杂度。
    
    这个题目等价于求一个序列与其排序的最长自序列
"""

import random
#import pdb; pdb.set_trace()

def LCS(x, y):
    #print x,y
    if len(x) == 0 or len(y) == 0:
        return ""
    else:
        a = x[0]
        b = y[0]
        if (a == b):
            return LCS(x[1:], y[1:]) + str(a)
        else:
            return cxMax(LCS(x[1:], y), LCS(x, y[1:]))

def cxMax(a, b):
    if len(a) >= len(b):
        return a
    else:
        return b

if  __name__ == '__main__':
    nums = range(1,10)
    sortnums = range(1,10)
    random.shuffle(sortnums)
    
    d = LCS(sortnums,nums)

    print "one list is: ",sortnums
    print "another list is: ",nums
    print 'LCS is:%s' % d[::-1]
