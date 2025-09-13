

#------------------#
# ROTASYON İŞLEMİ 
#------------------#

import cv2
import numpy as np

img = cv2.imread(r"materyal\yazi.png")

row = img.shape[0] # satır sayısı
col = img.shape[1] # sütun sayısı

M1 = cv2.getRotationMatrix2D((col/2, row/2), 45, 1) # 45 derece döndürme işlemi
M2 = cv2.getRotationMatrix2D((col/2, row/2), -90, 1) # -90 derece döndürme işlemi

rotated1 = cv2.warpAffine(img, M1, (col, row)) # warpAffine fonksiyonu ile döndürme işlemi yapılır.
rotated2 = cv2.warpAffine(img, M2, (col, row)) # warpAffine fonksiyonu ile döndürme işlemi yapılır.

cv2.imshow("Original", img)
cv2.imshow("Rotated 45", rotated1)
cv2.imshow("Rotated -90", rotated2)

cv2.waitKey(0)
cv2.destroyAllWindows()