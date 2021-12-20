#!/usr/bin/env python
# encoding: utf-8
"""
工厂方法
定义一个用于创建对象的接口, 让子类决定实例化哪个类
工厂方法使一个类的实例化延迟到其子类
如果存在变更, 改creator即可
"""
from abc import ABCMeta, abstractmethod
class BuildModel(metaclass=ABCMeta):
    """
    定义工厂方法所创建的对象接口
    """
    @abstractmethod
    def echo(self):
        pass
class BuildYoloV4(BuildModel):
    """
    具体的产品, 实现了BuildModel的接口
    """
    def echo(self):
        print(self.__class__.__name__)
class BuildYoloV5(BuildModel):
    """
    具体的产品, 实现了BuildModel的接口
    """
    def echo(self):
        #print("BuildModel B")
        print(self.__class__.__name__)
class Creator(metaclass=ABCMeta):
    """
    声明了工厂方法, 该方法返回一个BuildModel类型的对象
    """
    @abstractmethod
    def create(self):
        pass
class CreatorYoloV4(Creator):
    """
    重定义, 返回一个CreateNetwork实例
    """
    def create(self):
        return BuildYoloV4()
class CreatorYoloV5(Creator):
    def create(self):
        return BuildYoloV5()

class ManagerModel(object):
    def __init__(self):
        self._dict = {"yolov4": CreatorYoloV4().create(),
                      "yolov5": CreatorYoloV5().create()}

    def register(self, name, prototype):
        self._dict[name] = prototype

    def create(self, proto_name):
        return self._dict.get(proto_name)

if __name__ == '__main__':
    for i in range(100000000):
        # factory_a = CreatorYoloV4()
        # product = factory_a.create()
        # product.echo()

        factory_b = CreatorYoloV5()
        product = factory_b.create()
        product.echo()

        m = ManagerModel()
        m.register("yolov5", product)

        x = m.create("yolov5")
        x.echo()

