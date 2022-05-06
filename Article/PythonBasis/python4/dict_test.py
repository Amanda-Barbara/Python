#!/usr/bin/python
# coding=utf-8

tinydict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

print("字典值 : %s" % tinydict.items())

# 遍历字典列表
for key, values in tinydict.items():
    print(key, values)


tinydict = {'Name': 'Zara', 'Age': 7}
tinydict2 = {'Sex': 'female' }
tinydict3 = {'Age':18}

tinydict.update(tinydict2)
print(tinydict)
tinydict.update(tinydict3)
print(tinydict)