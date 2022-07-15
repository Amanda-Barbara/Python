# `typing`类型注解模块教程

## 类型别名
* 类型别名：类型别名通过将类型分配给别名来定义。在这个例子中， `Vector` 和 `List[float]` 将被视为可互换的同义词:
```python
from typing import List
Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)
```

## `typing` 模块中推出的 `TypeVar` 工厂函数实现泛型参数化
```python
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')      # Declare type variable

def first(l: Sequence[T]) -> T:   # Generic function
    return l[0]
```

## 用户定义的类可以定义为泛型类
```python
from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name #把字符串类型封装到了LoggedVar类中
        self.logger = logger #把日志模块Logger类型封装到了LoggedVar类中
        self.value = value #把泛型类型T封装到了LoggedVar类中

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)
```

## 参考链接
* 1 [python3.7的typing教程](https://docs.python.org/zh-cn/3.7/library/typing.html)
* 2 [python3.10的typing教程](https://docs.python.org/zh-cn/3/library/typing.html)