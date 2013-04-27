#!/usr/bin/python
#-*-coding:utf-8-*-

"""
    Given two sorted integer arrays, write an algorithm to get back the intersection.
    
"""

array1 = [2,5,8,23,56,89,125,169,196]
array2 = [5,8,9,34,78,123,125]

flag1 = 0
flag2 = 0
result = []

while flag1 != len(array1) and flag2 != len(array2):
    if array1[flag1] > array2[flag2]:
        flag2+=1
    elif array1[flag1] < array2[flag2]:
        flag1+=1
    else:
        result.append(array1[flag1])
        flag1+=1
        flag2+=1


print "array1:",array1
print "array2:",array2
print "result:",result
