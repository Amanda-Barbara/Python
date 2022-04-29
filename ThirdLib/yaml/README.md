# yaml模块详解

## load, dump
* load负责对输入的数据进行序列化处理
* dump负责对序列化的数据进行反序列处理
```python
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
if __name__ == '__main__':
    document = """
      a: 1
      b:
        c: 3
        d: 4
    """
    print(dump(load(document, Loader=Loader), Dumper=Dumper, default_flow_style=True))
    print(dump({'name': 'Silenthand Olleander', 'race': 'Human', 'traits': ['ONE_HAND', 'ONE_EYE']}, Dumper=Dumper, default_flow_style=True))
```

## python自定义类继承yaml.YAMLObject实现数据的序列化与反序列化
* yaml.YAMLObject用元类来注册一个构造器（也就是代码里的 init() 方法），让你把yaml节点转为Python对象实例，用表示器（也就是代码里的 repr() 函数）来让你把Python对象转为yaml节点
```python
import yaml
class Person(yaml.YAMLObject):
    yaml_tag = '!person'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '%s(name=%s, age=%d)' % (self.__class__.__name__, self.name, self.age)

if __name__ == '__main__':
    james = Person('James', 20)
    print(yaml.dump(james, default_flow_style=True))  # Python对象实例转为yaml
    lily = yaml.load('!person {name: Lily, age: 19}')
    print(lily)  # yaml转为Python对象实例
```


## yaml.add_constructor 和 yaml.add_representer函数
* 

## 参考链接
* 1 [PyYAML官方文档教程](https://pyyaml.org/wiki/PyYAMLDocumentation)
* 2 [yaml实现自定义类的序列化与反序列化教程](https://www.cnblogs.com/klb561/p/9326677.html)
