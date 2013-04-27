#!/usr/bin/python
#-*-coding:utf-8-*-

"""
    Array of 100 integers from 1 to 100, shuffled.  two integer is taken out, find them out.

    use bitmap algorithm
"""


import random

numbers = range(1,101)
random.shuffle(numbers)
remove_num1 = random.choice(numbers)
numbers.remove(remove_num1)
remove_num2 = random.choice(numbers)
numbers.remove(remove_num2)

bitarray = [0]*100

for i in numbers:
    bitarray[i-1] = 1

result = [i for i,j in enumerate(bitarray,1) if j == 0]

print "the remove numbers is: %s,%s"%(remove_num1,remove_num2)
print "the algorithm result is: %s,%s"%(result[0],result[1])
