#!/usr/bin/python
# -*-coding:utf-8 -*-

import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

print('*'*30)

d1 = dict(one=1, two=2)
d1['thr'] = {'t' : 3}
d1['four'] = 4
sub3 = d1['thr']
sub3['t'] = 8
print(d1)
sub4 = d1['four'] #如果d1['four']只是一个普通变量，sub4则相当于深拷贝
sub4 = 9
print(sub4)
print(d1)