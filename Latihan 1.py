# Nama: Yoga Satria Nugraha Kusmayadi
# NIM: 1217070087

import cv2
import numpy as np
image = cv2.imread("kucing.jpg")
b,g,r = cv2.split(image)
matriks0 = np.zeros(image.shape[:2],image.dtype)
m = matriks0
merah = cv2.merge([m,m,r])
cv2.imshow('Citra red channel', merah)
cv2.waitKey(0)