# `opencv`图像处理教程
* OpenCV是一个基于BSD许可（开源）发行的跨平台计算机视觉和机器学习软件库， 它轻量级而且高效——由一系列 C 函数和少量 C++ 类构成。

## [`cv2.threshold`](https://www.bilibili.com/video/BV1PV411774y?p=9&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)函数对图像设置阈值参数进行过滤操作

## [`cv2.erode`图像腐蚀操作](https://www.bilibili.com/video/BV1PV411774y?p=12&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)
* `kernel_size`大小元素值为1的卷积核对二值图像进行滑动窗口卷积操作，做完卷积后的矩阵中只要有一个元素值为0，则这一块被卷积的区域则置0处理。

## [`cv2.dilate`图像膨胀操作](https://www.bilibili.com/video/BV1PV411774y?p=12&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)
* `kernel_size`大小元素值为1的卷积核对二值图像进行滑动窗口卷积操作，做完卷积后的矩阵中只要有一个元素值为0，则这一块被卷积的区域则置1处理。

## [`形态学操作之开运算与闭运算`](https://www.bilibili.com/video/BV1PV411774y?p=14&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)
* 开运算是指对二值图先进行腐蚀再进行膨胀操作，闭运算则相反。
```python
kernel = np.ones((5,5), np.unit8)
opening = cv2.morphorlogyEx(img, cv2.MORPO_OPEN, kernel)
closing = cv2.morphorlogyEx(img, cv2.MORPO_ClOSE, kernel)
img_statck = np.vstatck((img, opening, closing))

```

## 


## 参考链接
* 1 [`opencv`视频教程](https://www.bilibili.com/video/BV1PV411774y?p=9&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)
* 2 [`opencv`视频教程代码](https://github.com/Amanda-Barbara/opencv_tutorial)
