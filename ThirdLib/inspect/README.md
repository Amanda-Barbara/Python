# inspect模块代码解读

## getfullargspec函数
* 返回参数func所需的参数
```python
FullArgSpec = namedtuple('FullArgSpec',
    'args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations')

def getfullargspec(func):
    ...
    return FullArgSpec(posonlyargs + args, varargs, varkw, defaults,
                       kwonlyargs, kwdefaults, annotations)
```

## 参考链接
* 1 []()