# matplotlib模块解析

## pyplot在图像中绘制曲线，需要改变y轴朝向
```python
plt.gca().invert_xaxis() # x轴方向向左
plt.gca().invert_yaxis() # y轴方向向下
```
