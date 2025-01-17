# 一、字典(Dictionary) #

## 1、什么是 dict（字典） ##

上一章节，我们学习了列表（List） 和 元组（tuple） 来表示有序集合。

而我们在讲列表（list）的时候，我们用了列表（list） 来存储用户的姓名。

```python
name = ['一点水', '两点水', '三点水', '四点水', '五点水']
```

那么如果我们为了方便联系这些童鞋，要把电话号码也添加进去，该怎么做呢？

用 list 可以这样子解决：

```python
name = [['一点水', '131456780001'], ['两点水', '131456780002'], ['三点水', '131456780003'], ['四点水', '131456780004'], ['五点水', '131456780005']]
```

但是这样很不方便，我们把电话号码记录下来，就是为了有什么事能及时联系上这些童鞋。

如果用列表来存储这些，列表越长，我们查找起来耗时就越长。

这时候就可以用 dict （字典）来表示了，Python 内置了 字典（dict），dict 全称 dictionary，如果学过 Java ，字典就相当于 JAVA 中的 map，使用键-值（key-value）存储，具有极快的查找速度。

```python
name = {'一点水': '131456780001', '两点水': '131456780002', '三点水': '131456780003', '四点水': '131456780004', '五点水': '131456780005'}
```



## 2、dict （字典）的创建 ##

字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：

```python
dict = {key1 : value1, key2 : value2 }
```

注意：键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的。

创建 dict（字典）实例：

```python
dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333'}
dict2={'abc':1234,1234:'abc'}
```



## 3、访问 dict （字典） ##

我们知道了怎么创建列表了，回归到一开始提出到的问题，为什么使用字典能让我们很快的找出某个童鞋的电话呢？



```python
name = {'一点水': '131456780001', '两点水': '131456780002', '三点水': '131456780003', '四点水': '131456780004', '五点水': '131456780005'}

print(name['两点水'])
```


输出的结果：

```
131456780002
```

可以看到，如果你知道某个人的名字，也就是 key 值， 就能很快的查找到他对应的电话号码，也就是 Value 。

这里需要注意的一点是：如果字典中没有这个键，是会报错的。



## 4、修改 dict （字典） ##

向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对

```python
#-*-coding:utf-8-*-
dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333'}
print(dict1)
# 新增一个键值对
dict1['jack']='444444'
print(dict1)
# 修改键值对
dict1['liangdianshui']='555555'
print(dict1)
```

输出的结果：

```
{'liangdianshui': '111111', 'twowater': '222222', '两点水': '333333'}
{'liangdianshui': '111111', 'twowater': '222222', '两点水': '333333', 'jack': '444444'}
{'liangdianshui': '555555', 'twowater': '222222', '两点水': '333333', 'jack': '444444'}
```

## 5、删除 dict （字典） ##

通过 `del` 可以删除 dict （字典）中的某个元素，也能删除 dict （字典）

通过调用 `clear()` 方法可以清除字典中的所有元素

```python
#-*-coding:utf-8-*-
dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333'}
print(dict1)
# 通过 key 值，删除对应的元素
del dict1['twowater']
print(dict1)
# 删除字典中的所有元素
dict1.clear()
print(dict1)
# 删除字典
del dict1
```

输出的结果：

```
{'liangdianshui': '111111', 'twowater': '222222', '两点水': '333333'}
{'liangdianshui': '111111', '两点水': '333333'}
{}
```

## 6、 dict （字典）使用时注意的事项 ##

(1) dict （字典）是不允许一个键创建两次的，但是在创建 dict （字典）的时候如果出现了一个键值赋予了两次，会以最后一次赋予的值为准

例如：

```python
#-*-coding:utf-8-*-
dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333','twowater':'444444'}
print(dict1)
print(dict1['twowater'])
```

输出的结果：

```
{'liangdianshui': '111111', 'twowater': '444444', '两点水': '333333'}
444444
```


(2) dict （字典）键必须不可变，可是键可以用数字，字符串或元组充当，但是就是不能使用列表

例如：

```python
#-*-coding:utf-8-*-
dict1={'liangdianshui':'111111' ,123:'222222' ,(123,'tom'):'333333','twowater':'444444'}
print(dict1)
```

输出结果：

```
{'liangdianshui': '111111', 123: '222222', (123, 'tom'): '333333', 'twowater': '444444'}
```

(3) dict 内部存放的顺序和 key 放入的顺序是没有任何关系

和 list 比较，dict 有以下几个特点：

* 查找和插入的速度极快，不会随着key的增加而变慢

* 需要占用大量的内存，内存浪费多

而list相反：

* 查找和插入的时间随着元素的增加而增加

* 占用空间小，浪费内存很少


## 7、dict （字典） 的函数和方法 ##

|方法和函数|描述|
|---------|--------|
|len(dict)|计算字典元素个数|
|str(dict)|输出字典可打印的字符串表示|
|type(variable)|返回输入的变量类型，如果变量是字典就返回字典类型|
|dict.clear()|删除字典内所有元素|
|dict.copy()|返回一个字典的浅复制|
|dict.values()|以列表返回字典中的所有值|
|popitem()|随机返回并删除字典中的一对键和值|
|dict.items()|以列表返回可遍历的(键, 值) 元组数组|

## get()方法
* Python 字典(Dictionary) get() 函数返回指定键的值
```python
dict.get(key, default=None)
```
* 返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。
```python
#!/usr/bin/python

dict = {'Name': 'Runoob', 'Age': 27}

print "Value : %s" %  dict.get('Age')
print "Value : %s" %  dict.get('Sex', "Not Available")
print dict.get('with_net', True)
```
输出结果是
```text
Value : 27
Value : Not Available
True
```
## update方法(添加或更新键值)
* Python 字典(Dictionary) update() 函数把字典dict2的键/值对更新到dict里

```shell
#!/usr/bin/python
tinydict = {'Name': 'Zara', 'Age': 7}
tinydict2 = {'Sex': 'female' }
tinydict3 = {'Age':18}

tinydict.update(tinydict2)
print(tinydict)
tinydict.update(tinydict3)
print(tinydict)
```
* `tinydict`字典中没有`tinydict2`中的键，则向`tinydict`字典对象中添加`tinydict2`的键值
* `tinydict`字典中有`tinydict3`中的键，则向`tinydict`字典对象中更新`tinydict3`的键值
```text
Value : {'Age': 7, 'Name': 'Zara', 'Sex': 'female'}
```
## `items方法`
* dict.items()返回可遍历的(键, 值)元组数组
```python
#!/usr/bin/python
# coding=utf-8
 
tinydict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
 
print("字典值 : %s" %  tinydict.items())
 
# 遍历字典列表
for key,values in  tinydict.items():
    print(key,values)
```

## 参考链接
* 1 [dict的get()方法使用](https://www.runoob.com/python/att-dictionary-get.html)
* 2 [update方法](https://www.runoob.com/python/att-dictionary-update.html)





