# `__init__(*args, **kwargs)`参数使用说明

## *args接受一个可变元组类型的对象，**kwargs接受一个可变字典类型的对象，二者使用时不冲突。
```python
    yolov4_pdr = {0: 'HELMET', 1: 'HEAD', 2: 'FIRE', 3: 'REFLECTIVE_CLOTHES', 4: 'PERSON'}
    labels_info1 = {'yolov4_pdr': yolov4_pdr}
    pdr = ObjectDetection(labels_info=labels_info1) #使用**kwargs格式接受参数
```

## 参考链接
* 1 [args与kwargs的区别](https://www.cnblogs.com/yunguoxiaoqiao/p/7626992.html)
