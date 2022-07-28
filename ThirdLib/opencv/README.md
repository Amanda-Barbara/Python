# `opencv`图像处理教程
* OpenCV是一个基于BSD许可（开源）发行的跨平台计算机视觉和机器学习软件库， 它轻量级而且高效——由一系列 C 函数和少量 C++ 类构成。

## [`cv2.threshold`](https://www.bilibili.com/video/BV1PV411774y?p=9&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)函数对图像设置阈值参数进行过滤操作

## [`cv2.erode`图像腐蚀操作](https://www.bilibili.com/video/BV1PV411774y?p=12&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)
* `kernel_size`大小元素值为1的卷积核对原图像进行滑动窗口卷积操作，做完卷积后的矩阵中只要有一个元素值为0，则这一块被卷积的区域则置0处理。

## [`cv2.dilate`图像膨胀操作](https://www.bilibili.com/video/BV1PV411774y?p=12&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)
* `kernel_size`大小元素值为1的卷积核对原图像进行滑动窗口卷积操作，做完卷积后的矩阵中只要有一个元素值为0，则这一块被卷积的区域则置1处理。

## [`形态学操作之开运算与闭运算`](https://www.bilibili.com/video/BV1PV411774y?p=14&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)
* 开运算是指对原图先进行腐蚀再进行膨胀操作，闭运算则相反。
```python
kernel = np.ones((5,5), np.unit8)
opening = cv2.morphorlogyEx(img, cv2.MORPO_OPEN, kernel)
closing = cv2.morphorlogyEx(img, cv2.MORPO_ClOSE, kernel)
img_statck = np.vstatck((img, opening, closing))
```

## [`形态学操作之梯度运算`](https://www.bilibili.com/video/BV1PV411774y?p=15&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)
* 梯度运算是指对原图分别执行腐蚀与膨胀的操作，然后再对返回的结果执行按位异或的操作即获得原图边缘的梯度信息。
```python
# 梯度运算
kernel = np.ones((7, 7), np.uint8)
dilate = cv2.dilate(circle,kernel=kernel,iterations=5)
erosion = cv2.erode(circle,kernel=kernel,iterations=5)
dilate_erosion_xor = cv2.bitwise_xor(dilate, erosion)
res1 = np.hstack((circle, dilate))
res2 = np.hstack((erosion, dilate_erosion_xor))
gradient_res1 = np.vstack((res1, res2))

# 使用形态学函数cv2.morphologyEx直接进行梯度运算操作
gradient = cv2.morphologyEx(circle, cv2.MORPH_GRADIENT, kernel=kernel)
gradient_vs = np.hstack((dilate_erosion_xor, gradient))
```
* 执行[bitwiseTest.py](src/bitwiseTest.py)查看结果。

## [`形态学操作之礼帽与黑帽运算`](https://www.bilibili.com/video/BV1PV411774y?p=16&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)
* 礼帽运算是指对原图进行开运算（先腐蚀后膨胀）去除“胡须”信息，然后再与原图进行按位异或操作最终可保留“胡须”信息
```python
img = cv2.imread('01_Picture/05_Dige.png')
kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
tophat2 = cv2.bitwise_xor(img, opening)
tophat_joint = np.hstack((tophat, tophat2))
```
* 黑帽运算是指对原图进行闭运算（先膨胀后腐蚀）对原图边界做轻微扰动，然后再与原图执行按位异或的操作最终获取到原图的边界信息。
```python
img = img = cv2.imread('01_Picture/05_Dige.png')
kernel = np.ones((5,5),np.uint8)
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel=kernel)
blackhat2 = cv2.bitwise_xor(img, closing)
blackhat_joint = np.hstack((blackhat, blackhat2))
```
* 执行[14_top_hat.py](opencv_tutorial/14_top_hat.py)查看结果

## 

## 参考链接
* 1 [`opencv`视频教程](https://www.bilibili.com/video/BV1PV411774y?p=9&vd_source=df8b73f15b5a0311fd8a1646ccd07daf)
* 2 [`opencv`视频教程代码](https://github.com/Amanda-Barbara/opencv_tutorial)
