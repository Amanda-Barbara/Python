# [yield生成器](https://www.runoob.com/w3cnote/python-yield-used-analysis.html)

> 原文：http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained
>
> 注：这是一篇 stackoverflow 上一个火爆帖子的译文

## 通俗理解
* `yield`返回一个迭代器，每调用一次迭代器则返回一次结果，节省内存占用，

## 问题 ##

Python 关键字 yield 的作用是什么？用来干什么的？

比如，我正在试图理解下面的代码:

```Python
def node._get_child_candidates(self, distance, min_dist, max_dist):
    if self._leftchild and distance - max_dist < self._median:
        yield self._leftchild
    if self._rightchild and distance + max_dist >= self._median:
        yield self._rightchild
```


下面的是调用:


```python
result, candidates = list(), [self]
while candidates:
    node = candidates.pop()
    distance = node._get_dist(obj)
    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
return result
```

当调用 ```_get_child_candidates``` 的时候发生了什么？返回了一个列表？返回了一个元素？被重复调用了么？ 什么时候这个调用结束呢？


## 回答

为了理解什么是 yield ,你必须理解什么是生成器。在理解生成器之前，让我们先走近迭代。

**可迭代对象**

当你建立了一个列表，你可以逐项地读取这个列表，这叫做一个可迭代对象:

```Python
>>> mylist = [1, 2, 3]
>>> for i in mylist :
...    print(i)
1
2
3
```

mylist 是一个可迭代的对象。当你使用一个列表生成式来建立一个列表的时候，就建立了一个可迭代的对象:

```python
>>> mylist = [x*x for x in range(3)]
>>> for i in mylist :
...    print(i)
0
1
4
```

所有你可以使用 ```for .. in ..``` 语法的叫做一个迭代器：列表，字符串，文件……你经常使用它们是因为你可以如你所愿的读取其中的元素，但是你把所有的值都存储到了内存中，如果你有大量数据的话这个方式并不是你想要的。

**生成器**

生成器是可以迭代的，但是你 只可以读取它一次 ，因为它并不把所有的值放在内存中，它是实时地生成数据:

```python
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator :
...    print(i)
0
1
4
```

看起来除了把 [] 换成 () 外没什么不同。但是，你不可以再次使用 ```for i in mygenerator``` , 因为生成器只能被迭代一次：先计算出0，然后继续计算1，然后计算4，一个跟一个的…

**yield 关键字**

yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。

```python
>>> def createGenerator() :
...    mylist = range(3)
...    for i in mylist :
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
```

这个例子没什么用途，但是它让你知道，这个函数会返回一大批你只需要读一次的值.

为了精通 yield ,你必须要理解：当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象，这有点蹊跷不是吗。

那么，函数内的代码什么时候执行呢？当你使用for进行迭代的时候.

现在到了关键点了！

第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值作为第一次迭代的返回值. 然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。

如果生成器内部没有定义 yield 关键字，那么这个生成器被认为成空的。这种情况可能因为是循环进行没了，或者是没有满足 if/else 条件。

**回到你的代码**

生成器:

```Python
# Here you create the method of the node object that will return the generator
def node._get_child_candidates(self, distance, min_dist, max_dist):

  # Here is the code that will be called each time you use the generator object :

  # If there is still a child of the node object on its left
  # AND if distance is ok, return the next child
  if self._leftchild and distance - max_dist < self._median:
            yield self._leftchild

  # If there is still a child of the node object on its right
  # AND if distance is ok, return the next child
  if self._rightchild and distance + max_dist >= self._median:
                yield self._rightchild

  # If the function arrives here, the generator will be considered empty
  # there is no more than two values : the left and the right children
```


调用者:

```Python
# Create an empty list and a list with the current object reference
result, candidates = list(), [self]

# Loop on candidates (they contain only one element at the beginning)
while candidates:

    # Get the last candidate and remove it from the list
    node = candidates.pop()

    # Get the distance between obj and the candidate
    distance = node._get_dist(obj)

    # If distance is ok, then you can fill the result
    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)

    # Add the children of the candidate in the candidates list
    # so the loop will keep running until it will have looked
    # at all the children of the children of the children, etc. of the candidate
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))

return result
```

这个代码包含了几个小部分：

* 我们对一个列表进行迭代，但是迭代中列表还在不断的扩展。它是一个迭代这些嵌套的数据的简洁方式，即使这样有点危险，因为可能导致无限迭代。 `candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))` 穷尽了生成器的所有值，但 while 不断地在产生新的生成器，它们会产生和上一次不一样的值，既然没有作用到同一个节点上.
* `extend()` 是一个迭代器方法，作用于迭代器，并把参数追加到迭代器的后面。


通常我们传给它一个列表参数:


```Python
>>> a = [1, 2]
>>> b = [3, 4]
>>> a.extend(b)
>>> print(a)
[1, 2, 3, 4]
```


但是在你的代码中的是一个生成器，这是不错的，因为：

* 你不必读两次所有的值
* 你可以有很多子对象，但不必叫他们都存储在内存里面。


并且这很奏效，因为 Python 不关心一个方法的参数是不是个列表。Python 只希望它是个可以迭代的，所以这个参数可以是列表，元组，字符串，生成器... 这叫做 `duck typing`,这也是为何 Python 如此棒的原因之一，但这已经是另外一个问题了...

你可以在这里停下，来看看生成器的一些高级用法:

**控制生成器的穷尽**

```Python
>>> class Bank(): # let's create a bank, building ATMs
...    crisis = False
...    def create_atm(self) :
...        while not self.crisis :
...            yield "$100"
>>> hsbc = Bank() # when everything's ok the ATM gives you as much as you want
>>> corner_street_atm = hsbc.create_atm()
>>> print(corner_street_atm.next())
$100
>>> print(corner_street_atm.next())
$100
>>> print([corner_street_atm.next() for cash in range(5)])
['$100', '$100', '$100', '$100', '$100']
>>> hsbc.crisis = True # crisis is coming, no more money!
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> wall_street_atm = hsbc.create_atm() # it's even true for new ATMs
>>> print(wall_street_atm.next())
<type 'exceptions.StopIteration'>
>>> hsbc.crisis = False # trouble is, even post-crisis the ATM remains empty
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> brand_new_atm = hsbc.create_atm() # build a new one to get back in business
>>> for cash in brand_new_atm :
...    print cash
$100
$100
$100
$100
$100
$100
$100
$100
$100
...
```


对于控制一些资源的访问来说这很有用。

**Itertools,你最好的朋友**

itertools 包含了很多特殊的迭代方法。是不是曾想过复制一个迭代器?串联两个迭代器？把嵌套的列表分组？不用创造一个新的列表的 zip/map?

只要 import itertools

需要个例子？让我们看看比赛中4匹马可能到达终点的先后顺序的可能情况:

```python
>>> horses = [1, 2, 3, 4]
>>> races = itertools.permutations(horses)
>>> print(races)
<itertools.permutations object at 0xb754f1dc>
>>> print(list(itertools.permutations(horses)))
[(1, 2, 3, 4),
 (1, 2, 4, 3),
 (1, 3, 2, 4),
 (1, 3, 4, 2),
 (1, 4, 2, 3),
 (1, 4, 3, 2),
 (2, 1, 3, 4),
 (2, 1, 4, 3),
 (2, 3, 1, 4),
 (2, 3, 4, 1),
 (2, 4, 1, 3),
 (2, 4, 3, 1),
 (3, 1, 2, 4),
 (3, 1, 4, 2),
 (3, 2, 1, 4),
 (3, 2, 4, 1),
 (3, 4, 1, 2),
 (3, 4, 2, 1),
 (4, 1, 2, 3),
 (4, 1, 3, 2),
 (4, 2, 1, 3),
 (4, 2, 3, 1),
 (4, 3, 1, 2),
 (4, 3, 2, 1)]
```

**了解迭代器的内部机理**

迭代是一个实现可迭代对象(实现的是 `__iter__()` 方法)和迭代器(实现的是 `__next__()` 方法)的过程。可迭代对象是你可以从其获取到一个迭代器的任一对象。迭代器是那些允许你迭代可迭代对象的对象。

* yield 的例子来源于文件读取。如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。好的方法是利用固定长度的缓冲区来不断读取文件内容。
```python
def read_file(fpath): 
    BLOCK_SIZE = 1024 
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                yield block 
            else: 
                return
```

```python
import numpy as np
from paddle.io import IterableDataset

# define a random dataset
class RandomDataset(IterableDataset):
    def __init__(self, num_samples):
        self.num_samples = num_samples

    def __iter__(self):
        for i in range(self.num_samples):
            image = np.random.random([784]).astype('float32')
            label = np.random.randint(0, 9, (1, )).astype('int64')
            yield image, label

dataset = RandomDataset(10)
for img, lbl in dataset:
    print(img, lbl)


def _accumulate(iterable, fn=lambda x, y: x * y):
    """
    Return running totals
    
    Args:
        iterable: any iterable object for example dataset.
        y (x): one element in the iterable object.
        fn (x, y): Defaults to lambdax.

    Yields:
        yields total from beginning iterator to current iterator.

    Example code:
    
        .. code-block:: python
        
            _accumulate([1,2,3,4,5]) --> 1 3 6 10 15
            _accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    """
#把list、dict、str等Iterable变成Iterator可以使用iter()函数，例如for c in iter('abc'):
    it = iter(iterable) 
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = fn(total, element)
        yield total


if __name__ == "__main__":
    for i in _accumulate([1,2,3,4,5]):
        print(i)
```

* `yield`中途返回，下一次程序遍历则从上一次中途返回后的第一条语句开始执行
```python
    def __iter__(self):
        batch_indices = []
        for idx in self.sampler:
            batch_indices.append(idx)
            if len(batch_indices) == self.batch_size:
                yield batch_indices #返回batch_indices结果
                batch_indices = [] #下一次遍历从此语句开始执行
        if not self.drop_last and len(batch_indices) > 0:
            yield batch_indices
```
## 参考链接
* 1 [yield使用浅析](https://www.runoob.com/w3cnote/python-yield-used-analysis.html)
* 2 [Iterable可迭代对象的解释](https://www.liaoxuefeng.com/wiki/1016959663602400/1017323698112640)
