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

## add_constructor函数
* 

## 参考链接
* 1 [PyYAML官方文档教程](https://pyyaml.org/wiki/PyYAMLDocumentation)