# Nama: Yoga Satria Nugraha Kusmayadi
# NIM: 1217070087

import cv2
import numpy as np
image = cv2.imread("kucing.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
MatriksSatu = np.ones(image.shape[:2],image.dtype)*100

citraPenjumlahan = cv2.add(gray,MatriksSatu)
cv2.imshow('Citra', gray)
cv2.imshow('Citra Penjumlahan', citraPenjumlahan) 
cv2.waitKey(0)