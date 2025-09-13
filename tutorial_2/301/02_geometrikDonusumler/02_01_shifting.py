

#------------------------------#
# SHİFTİNG (KAYDIRMA) İŞLEMİ
#------------------------------#

import cv2
import numpy as np

img = cv2.imread(r"materyal\yazi.png")

#rows, cols, ch = img.shape
row = img.shape[0] # satır sayısı 
col = img.shape[1] # sütun sayısı 

M= np.float32([[1,0,300],[0,1,90]]) # 100 sağa, 50 aşağı kaydırma

shifted = cv2.warpAffine(img, M, (col, row)) # warpAffine fonksiyonu ile kaydırma işlemi yapılır.

cv2.imshow("Original", img)
cv2.imshow("Shifted", shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()