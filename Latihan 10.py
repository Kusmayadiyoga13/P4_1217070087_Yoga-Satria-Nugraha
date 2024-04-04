# Nama: Yoga Satria Nugraha Kusmayadi
# NIM: 1217070087

import cv2
import numpy as np

image = cv2.imread('kucing.jpg')
height, width = image.shape[:2]
M = np.float32([[1, 0, 100], [0, 1, 50]])
image_translation = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Citra', image)
cv2.imshow("Citra Hasil Translasi", image_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
