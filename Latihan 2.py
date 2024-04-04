# Nama: Yoga Satria Nugraha Kusmayadi
# NIM: 1217070087

import cv2
import numpy as np
image = cv2.imread("kucing.jpg")
max_pixel_value = 255
inverted_image =max_pixel_value - image
cv2.imshow('Original image', image)
cv2.imshow('citra negatif', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()