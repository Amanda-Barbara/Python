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


## 参考链接
* 1 [python3.7的typing教程](https://docs.python.org/zh-cn/3.7/library/typing.html)
* 2 [python3.10的typing教程](https://docs.python.org/zh-cn/3/library/typing.html)