import cv2
import numpy as np

# 读取图片
img = cv2.imread("image.jpg")

# 将图片转换为灰度
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用阈值将图片二值化
retval, thresh_img = cv2.threshold(gray_img, 120, 255, cv2.THRESH_BINARY)

# 检测轮廓
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

# 显示图片
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()