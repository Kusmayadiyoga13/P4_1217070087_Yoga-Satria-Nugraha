# Nama: Yoga Satria Nugraha Kusmayadi
# NIM: 1217070087

import cv2
import numpy as np

image = cv2.imread('kucing.jpg')
(height, width) = image.shape[0:2]
RotasiMatriks = cv2.getRotationMatrix2D((width/2, height/2), -90, 0.5)
RotasiCitra = cv2.warpAffine(image, RotasiMatriks, (width, height))
cv2.imshow('Citra Rotasi', RotasiCitra)
cv2.waitKey(0)
cv2.destroyAllWindows()
