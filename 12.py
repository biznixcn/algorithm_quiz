#!/usr/bin/python
#-*-coding:utf-8-*-

def solve():
    '''
        电脑上的每个字符都有一一个唯一一编码,通用的标准是ASCII (American Standard Code for
    Information Interchange 美国信息交换标准编码)。例如大写A = 65, 星号(*) = 42,小写k =
    107。
    一一种现代加密方法是用一一个密钥中的给定值,与一一个文本文件中字符的ASCII值进行异或。使用
    异或方法的好处是对密文使用同样的加密密钥可以得到加密前的内容。例如,65 XOR 42 = 107,
    然后 107 XOR 42 = 65。
    对于不可攻破的加密,密钥的长度与明文信息的长度是一一样的,而且密钥是由随机的字节组成
    的。用户将加密信息和加密密钥保存在不同地方,只有在两部分都得到的情况下,信息才能被解
    密。
    不幸的是,这种方法对于大部分用户来说是不实用的。所以一一种修改后的方案是使用一一个密码作
    为密钥。如果密码比信息短,那么就将其不断循环直到明文的长度。平衡点在于密码要足够长来
    保证安全性,但是又要足够短使用户能够记得。
    你的任务很简单,因为加密密钥是由三个小写字母组成的。文件 https://gist.github.com/
    qingfeng/15dbd3f3f6d9563aa73a/raw/c096dcd54689b78e11d0439d412e15dbb81d548c/
    cipher1.txt 中包含了加密后的ASCII码,并且已知明文是由常用英语单词组成。使用该文件来解
    密信息,然后算出明文, 以及密码
    
        decrypt messages.
    '''
    
    def _combinators(_handle, items, n):
        if n==0:
            yield []
            return #这个必须有，用来控制终止条件
        for i, item in enumerate(items):#用来模拟多重for循环
            this_one = [ item ]
            for cc in _combinators(_handle, _handle(items, i), n-1):
                yield this_one + cc

    def selections(items, n):
        def keepAllItems(items, i):#通过他对for循环中每一项和对应的索引进行处理，返回for循环的内容
            return items
        return _combinators(keepAllItems, items, n)
    
    code = tuple(int(c) for c in open('cipher1.txt').read().split(','))
    
    def decrypt(code, password):
        l = len(password)
        return tuple(c ^ password[i % l] for i, c in enumerate(code))
    
    def text(code): return ''.join(chr(c) for c in code)
    
    for password in selections(tuple((ord(c) for c in list('abcdefghijklmnopqrstuvwxyz'))), 3):
        c = decrypt(code, password)
        t = text(c)
        if t.find(' the ') > 0:
            print "the code is: ","".join([chr(j) for j in password])
            print "the original messages is: ",t
            break

if __name__ == "__main__":
    solve()
