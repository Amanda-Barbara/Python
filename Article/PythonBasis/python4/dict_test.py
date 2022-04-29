#!/usr/bin/python
# coding=utf-8

tinydict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

print("字典值 : %s" % tinydict.items())

# 遍历字典列表
for key, values in tinydict.items():
    print(key, values)