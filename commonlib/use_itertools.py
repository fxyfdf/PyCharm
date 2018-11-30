#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

"""
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
"无限" 迭代器
"""

# natuals = itertools.count(1)
# for n in natuals:
#     print (n)
#     if n >= 100:
#         break
#
# cs = itertools.cycle('ABC')
# t = 10
# for c in cs:
#     print (c)
#     t = t - 1
#     if t == 0:
#         break

#######################################################################
"""
takewhile 
无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
"""
natuals = itertools.count(1)
print (natuals)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print (list(ns))

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
    print (c)





