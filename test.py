import cv2
from rotate import rotate
from move import move
from pitch import pitch

# 标定顺序为 旋转-俯仰角-平移-缩放(P.S.缩放几乎可以不考虑，因为4个镜头距离物体的远近几乎一样)
# 原图
img = cv2.imread('1.bmp')
# 旋转
rotated_img = rotate(img, 5)
# 移动
shifted_img = move(img, -50, 25)
# 放缩
resized_img = cv2.resize(img, None, fx=1.25, fy=1.25, interpolation=cv2.INTER_LINEAR)
# 俯仰角
pitched_img = pitch(img, 1, 0.25)

# 显示原图和调整后的图像
cv2.imshow('original image', img)
cv2.imshow('rotated image', rotated_img)
cv2.imshow('shifted image', shifted_img)
cv2.imshow('resized image', resized_img)
cv2.imshow('pitched image', pitched_img)

# 等待用户按下键盘按键关闭图像窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
