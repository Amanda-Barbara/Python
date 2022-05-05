# `__init__(*args, **kwargs)`参数使用说明

## *args接受一个可变元组类型的对象，**kwargs接受一个可变字典类型的对象，二者使用时不冲突。
```text
    yolov4_pdr = {0: 'HELMET', 1: 'HEAD', 2: 'FIRE', 3: 'REFLECTIVE_CLOTHES', 4: 'PERSON'}
    labels_info1 = {'yolov4_pdr': yolov4_pdr}
    pdr = ObjectDetection(labels_info=labels_info1) #使用**kwargs格式接受参数
```

## 类的成员变量可以在类的成员函数中进行声明和初始化，在对象中也可以访问和修改
```shell
python3 ./init_test.py
```

## 类对象可以在程序中添加自定义对象变量
```shell
python3 ./init_test.py
```
## 类变量和类的成员变量
* name1是类变量，可以由类名直接调用， 也可以有对象来调用，
  成员变量一定是以self.的形式给出的，因为self的含义就是代表实例对象
```shell
python ./init_test.py
```

## 参考链接
* 1 [args与kwargs的区别](https://www.cnblogs.com/yunguoxiaoqiao/p/7626992.html)
* 2 [**kwargs把键值传递给函数的形参使用](https://www.cnblogs.com/cwind/p/8996000.html)

