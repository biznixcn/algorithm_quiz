#!/usr/bin/python
#-*-coding:utf-8-*-

"""
    欧几里得算法
        分析：求最大公约数的算法思想：
        (1) 对于已知两数m，n，使得m>n；
        (2) m除以n得余数r；
        (3) 若r=0，则n为求得的最大公约数，算法结束；否则执行(4)；
        (4) m←n，n←r，再重复执行(2)。
        例如: 求 m=14 ,n=6 的最大公约数. m n r
"""

m,n = 14,6

def temp_divisor(m,n):
    r = m%n
    if r == 0:
        return n
    else:
        return temp_divisor(n,r)

print temp_divisor(m,n)
