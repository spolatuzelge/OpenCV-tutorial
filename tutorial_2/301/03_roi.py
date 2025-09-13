

#--------------------------#
# REGION OF INTEREST (ROI)
#--------------------------#

import cv2
import numpy as np

img = cv2.imread(r"materyal\yazi.png")

h , w = img.shape[:2] # yükseklik ve genişlik değerlerini alır.
imgCrop = img.copy() # orijinal görselin bir kopyasını alır.

roi = img[40:180, 50:1050] # ROI belirleme işlemi yapılır.
# img[y1:y2, x1:x2] : y1,y2 ve x1,x2 koordinatları arasındaki bölgeyi seçer.

print("Yükseklik:", h)
print("Genişlik:", w)
cv2.imshow("Original", img)
cv2.imshow("ROI", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()