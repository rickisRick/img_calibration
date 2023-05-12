import cv2
import numpy as np


def pitch(img, upordown, imgrange=0):
    height, width = img.shape[:2]
    imgrange /= 0.5
    # 确定原始图像上的四个点
    pt1 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    if upordown == 0:
        pt2 = np.float32([[-imgrange * width, 0], [(1 + imgrange) * width, 0], [0, height], [width, height]])
    else:
        pt2 = np.float32([[0, 0], [width, 0], [-imgrange * width, height], [(1 + imgrange) * width, height]])
    m = cv2.getPerspectiveTransform(pt1, pt2)
    return cv2.warpPerspective(img, m, (width, height))
