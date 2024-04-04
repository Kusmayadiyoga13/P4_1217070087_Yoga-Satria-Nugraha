# Nama: Yoga Satria Nugraha Kusmayadi
# NIM: 1217070087

import cv2

image = cv2.imread('kucing.jpg')
zoom_factor = 1.5 
height, width = image.shape[:2]
new_height = int(height * zoom_factor)
new_width = int(width * zoom_factor)
scaled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Original Image", image)
cv2.imshow("Image Zooming", scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
