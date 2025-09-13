

#---------------------------------------------------------#
# GÖRÜNTÜYÜ DİKEY VE YATAY OLARAK ÇEVİRME İŞLEMLERİ
#---------------------------------------------------------#

import cv2
import numpy as np

img = cv2.imread(r"materyal\logo.png")

#X Flip
x_flip = cv2.flip(img,0) # 0 -> x eksenine göre flip
cv2.imshow("x_flip",x_flip)
cv2.waitKey(0)

#Y Flip
y_flip = cv2.flip(img,1) # 1 -> y eksenine göre flip
cv2.imshow("y_flip",y_flip)
cv2.waitKey(0)

#XY Flip
xy_flip = cv2.flip(img,-1) # -1 -> x ve y eksenine göre flip
cv2.imshow("xy_flip",xy_flip)
cv2.waitKey(0)
