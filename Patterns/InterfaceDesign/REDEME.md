# python 接口设计方案

## `raiseNotImplementedError`模式
* 子类没有实现父类中指定要实现的方法，则会自动调用父类中的方法，而父类方法又是raise将错误抛出
  以paddlepaddle的dataset类设计为例
```python

class Dataset(object):
    """
    An abstract class to encapsulate methods and behaviors of datasets.

    All datasets in map-style(dataset samples can be get by a given key)
    should be a subclass of `paddle.io.Dataset`. All subclasses should
    implement following methods:

    :code:`__getitem__`: get sample from dataset with a given index. This
    method is required by reading dataset sample in :code:`paddle.io.DataLoader`.

    :code:`__len__`: return dataset sample number. This method is required
    by some implements of :code:`paddle.io.BatchSampler`

    see :code:`paddle.io.DataLoader`.

    Examples:
        
        .. code-block:: python

            import numpy as np
            from paddle.io import Dataset
            
            # define a random dataset
            class RandomDataset(Dataset):
                def __init__(self, num_samples):
                    self.num_samples = num_samples
            
                def __getitem__(self, idx):
                    image = np.random.random([784]).astype('float32')
                    label = np.random.randint(0, 9, (1, )).astype('int64')
                    return image, label
                
                def __len__(self):
                    return self.num_samples
            
            dataset = RandomDataset(10)
            for i in range(len(dataset)):
                print(dataset[i])

    """

    def __init__(self):
        pass

    def __getitem__(self, idx):
        raise NotImplementedError("'{}' not implement in class "\
                "{}".format('__getitem__', self.__class__.__name__))

    def __len__(self):
        raise NotImplementedError("'{}' not implement in class "\
                "{}".format('__len__', self.__class__.__name__))

```


## 参考链接
* 1 [raiseNotImplementedError模式](https://www.cnblogs.com/everfight/p/NotImplementedError.html)