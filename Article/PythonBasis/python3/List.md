# 一、List（列表） #

## 1、什么是 List （列表）

List （列表）是 Python 内置的一种数据类型。 它是一种有序的集合，可以随时添加和删除其中的元素。

那为什么要有 List （列表）呢？

我们用一个例子来说明。

现在有一个团队要出去玩，要先报名。如果用我们之前学过的知识，那么就是用一个字符串变量把他们都记录起来。

![](http://twowaterimage.oss-cn-beijing.aliyuncs.com/2019-08-31-080527.png)

但是这样太麻烦了，而且也不美观。

在编程中，一定要学会偷懒，避免「重复性工作」。如果有一百个成员，那么你及时是复制粘贴，也会把你写烦。

这时候就可以使用列表了。

![](http://twowaterimage.oss-cn-beijing.aliyuncs.com/2019-08-31-080835.png)

就这样，一行代码就可以存放 N 多个名字了。


## 2、怎么创建 List（列表） ##

从上面的例子可以分析出，列表的格式是这样的。

![](http://twowaterimage.oss-cn-beijing.aliyuncs.com/2019-08-31-081342.png)

其实列表就是用中括号 `[]` 括起来的数据，里面的每一个数据就叫做元素。每个元素之间使用逗号分隔。

而且列表的数据元素不一定是相同的数据类型。

比如：

```python
list1=['两点水','twowter','liangdianshui',123]
```

这里有字符串类型，还有整数类型。

我们尝试把他打印出来，看看打印的结果是怎样的。

![](http://twowaterimage.oss-cn-beijing.aliyuncs.com/2019-08-31-081912.png)

结果如下：

![](http://twowaterimage.oss-cn-beijing.aliyuncs.com/2019-08-31-081951.png)


## 3、如何访问 List（列表）中的值 ##

就像一开始的例子，我们有时候不需要把全部人员的姓名都打印出来，有时候我们需要知道第 3 个报名的人是谁？前两名报名的是谁？

那么怎么从列表中取出来呢？

换种问法就是，怎么去访问列表中的值？

这时候我们可以通过列表的下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符。

例如：

```python
name = ['一点水', '两点水', '三点水', '四点水', '五点水']

# 通过索引来访问列表
print(name[2])
# 通过方括号的形式来截取列表中的数据
print(name[0:2])
```

输出的结果：

![](http://twowaterimage.oss-cn-beijing.aliyuncs.com/2019-08-31-090321.png)

可见，我们需要知道知道 `name` 这个列表中第三个报名的是谁？只需要用 `name[2]`  就可以了。

这里你会问，为什么是 2 ，不是 3 呢？

这是因为在编程世界中，都是从 0 开始的，而不是我们生活习惯中从 1 开始。

所以需要知道第三个是谁？

那就是  `name[2]`  就可以了。

从例子来看，我们还把 `name[0:2]` 的结果打印出来了。

从打印结果来看，只打印了第一，第二个元素内容。

这里可能会有疑问？

为什么不是打印前三个啊，不是说 2 就是第 3 个吗？

那是因为这是**左闭右开**区间的。

所以 `name[0:2]` 的意思就是从第 0 个开始取，取到第 2 个，但是不包含第 2 个。

还是那句话，为了更好的理解，可以多去尝试，多去玩编程。

所以你可以尝试下下面的各种方式：

![](http://twowaterimage.oss-cn-beijing.aliyuncs.com/2019-08-31-091524.png)

看看输出的结果：

![](http://twowaterimage.oss-cn-beijing.aliyuncs.com/2019-08-31-091624.png)

根据输出的结果和上面讲到的知识，就很容易理解其中的一些用法了。




    ## 4、怎么去更新 List（列表） ##

还是一开始的例子，我们用代码记录了报名人的名字，那后面可能会有新人加入，也有可能会发现一开始写错名字了，想要修改。

这时候怎么办呢？

这时候可以通过索引对列表的数据项进行修改或更新，也可以使用 append() 方法来添加列表项。

```python
name = ['一点水', '两点水', '三点水', '四点水', '五点水']


# 通过索引对列表的数据项进行修改或更新
name[1]='2点水'
print(name)

# 使用 append() 方法来添加列表项
name.append('六点水')
print(name)
```

输出的结果：

![](http://twowaterimage.oss-cn-beijing.aliyuncs.com/2019-08-31-092406.png)





## 5、怎么删除 List（列表） 里面的元素 ##

那既然这样，肯定会有人中途退出的。

那么我们就需要在列表中，把他的名字去掉。

这时候使用 del 语句来删除列表的的元素

```python
name = ['一点水', '两点水', '三点水', '四点水', '五点水']

print(name)

# 使用 del 语句来删除列表的的元素
del name[3]
print(name)
```

输出的结果:

![](http://twowaterimage.oss-cn-beijing.aliyuncs.com/2019-08-31-092705.png)

你看输出的结果，列表中已经没有了 `四点水` 这个数据了。证明已经删除成功了。






## 6、List（列表）运算符 ##

列表对 `+`  和 `*`  的操作符与字符串相似。`+` 号用于组合列表，`*`  号用于重复列表。

|Python 表达式|结果|描述|
|-----------|-----|-----|
|len([1, 2, 3])|3|计算元素个数|
|[1, 2, 3] + [4, 5, 6]|	[1, 2, 3, 4, 5, 6]|	组合|
|['Hi!'] * 4|['Hi!', 'Hi!', 'Hi!', 'Hi!']|复制|
|3 in [1, 2, 3]|True|元素是否存在于列表中|
|for x in [1, 2, 3]: print x,|1 2 3|迭代|


## 7、List （列表）函数&方法 ##

|函数&方法|描述|
|----|----|
|len(list)|列表元素个数|
|max(list)|返回列表元素最大值|
|min(list)|返回列表元素最小值|
|list(seq)|将元组转换为列表|
|list.append(obj)|在列表末尾添加新的对象|
|list.count(obj)|统计某个元素在列表中出现的次数|
|list.extend(seq)|在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）|
|list.index(obj)|从列表中找出某个值第一个匹配项的索引位置|
|list.insert(index, obj)|将对象插入列表|
|list.pop(obj=list[-1])|移除列表中的一个元素（默认最后一个元素），并且返回该元素的值|
|list.remove(obj)|移除列表中的一个元素（参数是列表中元素），并且不返回任何值|
|list.reverse()|反向列表中元素|
|list.sort([func])|对原列表进行排序|


## 8、实例 ##


最后通过一个例子来熟悉了解 List 的操作

例子：

```python
#-*-coding:utf-8-*-
#-----------------------list的使用----------------------------------

# 1.一个产品，需要列出产品的用户，这时候就可以使用一个 list 来表示
user=['liangdianshui','twowater','两点水']
print('1.产品用户')
print(user)

# 2.如果需要统计有多少个用户，这时候 len() 函数可以获的 list 里元素的个数
len(user)
print('\n2.统计有多少个用户')
print(len(user))

# 3.此时，如果需要知道具体的用户呢？可以用过索引来访问 list 中每一个位置的元素，索引是0从开始的
print('\n3.查看具体的用户')
print(user[0]+','+user[1]+','+user[2])

# 4.突然来了一个新的用户，这时我们需要在原有的 list 末尾加一个用户
user.append('茵茵')
print('\n4.在末尾添加新用户')
print(user)

# 5.又新增了一个用户，可是这个用户是 VIP 级别的学生，需要放在第一位，可以通过 insert 方法插入到指定的位置
# 注意：插入数据的时候注意是否越界，索引不能超过 len(user)-1
user.insert(0,'VIP用户')
print('\n5.指定位置添加用户')
print(user)

# 6.突然发现之前弄错了，“茵茵”就是'VIP用户'，因此，需要删除“茵茵”；pop() 删除 list 末尾的元素
user.pop()
print('\n6.删除末尾用户')
print(user)

# 7.过了一段时间，用户“liangdianshui”不玩这个产品，删除了账号
# 因此需要要删除指定位置的元素，用pop(i)方法，其中i是索引位置
user.pop(1)
print('\n7.删除指定位置的list元素')
print(user)

# 8.用户“两点水”想修改自己的昵称了
user[2]='三点水'
print('\n8.把某个元素替换成别的元素')
print(user)

# 9.单单保存用户昵称好像不够好，最好把账号也放进去
# 这里账号是整数类型，跟昵称的字符串类型不同，不过 list 里面的元素的数据类型是可以不同的
# 而且 list 元素也可以是另一个 list
newUser=[['VIP用户',11111],['twowater',22222],['三点水',33333]]
print('\n9.不同元素类型的list数据')
print(newUser)

```

![list的使用](http://upload-images.jianshu.io/upload_images/2136918-65d31cae9f8bb34d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


* extend()函数的使用方法
```python
#!/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)

print "Extended List : ", aList ;
```
输出结果
```text
Extended List :  [123, 'xyz', 'zara', 'abc', 123, 2009, 'manni']
```

* list使用运算符`+`进行拼接
```python
[0, 0] + [1] * 3
```
输出是`[0, 0, 1, 1, 1]`

## `list`与`Sequence`的区别
```text
A list is a sequence but a sequence is not necessarily a list. A sequence is any type
```

## 参考链接
* 1 [extend使用方法](https://www.runoob.com/python/att-list-extend.html)
