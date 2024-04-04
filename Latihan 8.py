# Nama: Yoga Satria Nugraha Kusmayadi
# NIM: 1217070087

import cv2
import numpy as np

persegi = np.zeros((400, 400), dtype="uint8")
cv2.rectangle(persegi, (60, 60), (340, 340), 255, -1)
lingkaran = np.zeros((400, 400), dtype="uint8")
cv2.circle(lingkaran, (200, 200), 150, 255, -1)
operasiXOR = cv2.bitwise_xor(persegi, lingkaran)
cv2.imshow("Persegi", persegi)
cv2.imshow("Lingkaran", lingkaran)
cv2.imshow("Operasi XOR", operasiXOR)
cv2.waitKey(0)
cv2.destroyAllWindows()
