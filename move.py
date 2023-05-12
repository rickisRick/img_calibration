import cv2
import numpy as np


# 向右&向下为正方向
def move(img, xdir=0, ydir=0):
    m = np.float32([[1, 0, xdir], [0, 1, ydir]])
    return cv2.warpAffine(img, m, (img.shape[1], img.shape[0]))
