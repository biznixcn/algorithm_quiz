#!/usr/bin/python
#-*-coding:utf-8-*-

"""
    RLE(Run Length Encoding),即行程压缩算法,是一个针对无损压缩的非常简单的算法。它用重复 字节和重复的次数来简单描述、代替连续出现的重复字节。尽管简单并且对于通常的压缩非常低效,但 是由于非常适合有大量重复色块的图形,而且解压缩效率很高,因此应用较为广泛。 RLE 可以使用很 多不同的方法,最简单的做法是:对于不重复内容,不做转换,对于重复内容，用“控制字节+重复次 数+重复字节”三个字节表达。 请用任何你熟悉的编程语言，写出这种简单RLE压缩实现的代码。 不能使用任何有直接帮助的第三方库。
"""

import string

class RunLength:
    """Helper container class for string encoding"""
    def __init__(self, char, length=1):
        self.char = char
        self.length = length

    def __str__(self):
        if self.length <= 0:
            return ''
        if self.length == 1:
            return self.char
        if self.length >= 2:
            return (chr(255) + '9' + self.char)*(self.length//9) + \
                chr(255) + '%d'%(self.length%9) + self.char

def compress(plainText):
    """
        compress the plain text
    """
    
    compressedRuns = []
    current = RunLength('', 0)
    for char in plainText:
        if char == current.char:
            current.length += 1
        else:
            compressedRuns.append(str(current))
            current = RunLength(char)
    compressedRuns.append(str(current)) # Append the last run
    return ''.join(compressedRuns)

def decompress(compressedText):
    """
        decompress the compressed text
    """
    
    decompressedRuns = []
    i = 0
    while i != len(compressedText):
        if ord(compressedText[i]) == 255:
            decompressedRuns.append(int(compressedText[i+1])*compressedText[i+2])
            i+=3
        else:
            decompressedRuns.append(compressedText[i])
            i+=1

    return "".join(decompressedRuns)

if __name__ == "__main__":
    compress_str = "abccccc12333333333333333"
    print compress(compress_str)
    print decompress(compress(compress_str))
