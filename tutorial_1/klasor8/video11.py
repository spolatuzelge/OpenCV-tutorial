

" -------------- "
# Resim Döndürme
# [cv2.getRotationMatrix2D() ,]
" -------------- "

import cv2
import numpy as np

img = cv2.imread("materyal\\klasor8\\helikopter.png",0)
row , col = img.shape

M= cv2.getRotationMatrix2D((col/2,row/2),90,1) # 90 derece döndürme. Önce sütun ve satır değerlerini alır. Sonra derece ve ölçekleme değerlerini alır.

dst = cv2.warpAffine(img,M,(col,row)) # warpAffine() fonksiyonu ile döndürme işlemi yapılır.

cv2.imshow("Orjinal Resim",img)
cv2.imshow("Döndürülmüş Resim",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()