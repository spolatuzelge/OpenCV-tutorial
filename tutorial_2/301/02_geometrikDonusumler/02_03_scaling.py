

#------------------#
# SCALE İŞLEMİ
#------------------#

import cv2
import numpy as np

img = cv2.imread(r"materyal\yazi.png")

row = img.shape[0] # satır sayısı
col = img.shape[1] # sütun sayısı

scale1 =cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC) # 0.5 oranında küçültme işlemi
# resize(görsel , None, x oranı, y oranı, interpolation: kullanılacak interpolasyon yöntemi)
scale2 =cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) # 2 kat büyütme işlemi

cv2.imshow("Original", img)
cv2.imshow("Scale 0.5", scale1)
cv2.imshow("Scale 2", scale2)

cv2.waitKey(0)
cv2.destroyAllWindows()