import math
import cv2


# 图像旋转，正为逆时针，旋转角度为 角度制 而非 弧度制
def rotate(img, tilt_angle=0):
    # 获取图像尺寸
    height, width = img.shape[:2]

    # 创建仿射变换矩阵
    matrix = cv2.getRotationMatrix2D((width / 2, height / 2), tilt_angle, 1)

    # 进行仿射变换，调整旋转角度
    rtted = cv2.warpAffine(img, matrix, (width, height))

    # 旋转后放大的比例系数
    multiple = math.sqrt(1 + height * height / width / width) * math.cos(
        math.atan(height / width) - abs(tilt_angle) * math.pi / 180)

    # 做放大处理，使得旋转后的图像放大到原图大小，如rttdemo.png所示的部分(P.S.后续结合整体需要进行裁剪等操作)
    return cv2.resize(rtted, None, fx=multiple, fy=multiple, interpolation=cv2.INTER_LINEAR)
