import numpy as np
import cv2
 
# 在画布中心画了一个300*300像素的矩形，用白色填充
# 注意：这是一个二维矩阵，反映在图片上是单通道的
rectangle = np.zeros((300, 300), dtype="uint8")
# 第二个参数为矩形左上角的点的坐标，第三个参数为矩形右下角的点的坐标
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
# cv2.imshow("Rectangle", rectangle)
 
# 在画布中心画了一个半径150像素的圆圈，用白色填充
# 注意：这是一个二维矩阵，反映在图片上是单通道的
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
# cv2.imshow("Circle", circle)
 
# 按位与操作AND，取交集
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
# cv2.imshow("AND", bitwiseAnd)

# 按位或操作OR，取并集
bitwiseOr = cv2.bitwise_or(rectangle, circle)
# cv2.imshow("OR", bitwiseOr)

 
# 按位异或XOR，取并集后再去掉交集
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
# cv2.imshow("XOR", bitwiseXor)
 
# 按位非NOT
bitwiseNot = cv2.bitwise_not(circle)
# cv2.imshow("NOT", bitwiseNot)
 
# cv2.waitKey(0)  # 等待用户输入，按任意键即可
img_joint = np.hstack((bitwiseAnd, bitwiseOr, bitwiseXor, bitwiseXor, bitwiseNot))
print(1)

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
print(2)
