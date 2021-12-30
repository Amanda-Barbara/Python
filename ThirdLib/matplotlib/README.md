# matplotlib模块解析

## pyplot在图像中绘制曲线，需要改变y轴朝向
```python
plt.gca().invert_xaxis() # x轴方向向左
plt.gca().invert_yaxis() # y轴方向向下
```

## pyplot在一个显示窗口中绘制多个图像
```python
import numpy as np
import matplotlib.pyplot as plt

def display_multiple_img(images, rows = 1, cols=1):
    figure, ax = plt.subplots(nrows=rows,ncols=cols )
    for ind,title in enumerate(images):
        ax.ravel()[ind].imshow(images[title])
        ax.ravel()[ind].set_title(title)
        ax.ravel()[ind].set_axis_off()
    plt.tight_layout()
    plt.show()

total_images = 4
images = {'Image'+str(i): np.random.rand(100, 100) for i in range(total_images)}

display_multiple_img(images, 2, 2)
```

## 参考链接
* 1 [subplots绘制多个图像](https://www.delftstack.com/zh/howto/matplotlib/how-to-display-multiple-images-in-one-figure-correctly-in-matplotlib/)
