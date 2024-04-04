# Nama: Yoga Satria Nugraha Kusmayadi
# NIM: 1217070087

import cv2
import numpy as np

image = cv2.imread('kucing.jpg')
flip_hor = cv2.flip(image, 1)
flip_ver = cv2.flip(image, 0)
flip_verhor = cv2.flip(image, -1)
cv2.imshow("Citra Asli", image)
cv2.imshow('Citra Flip Horizontal', flip_hor)
cv2.imshow('Citra Flip Vertical', flip_ver)
cv2.imshow("Citra Flip Vertical-Horizontal", flip_verhor)
cv2.waitKey(0)
cv2.destroyAllWindows()
