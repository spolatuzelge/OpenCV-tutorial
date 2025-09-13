

" ------------- "
# Tresholding
" ------------- "

import cv2
import numpy as np

img = cv2.imread("materyal\\klasor8\\helikopter2.png",0) #gray scale olarak okuma işlemi yapılır.

ret , th1 = cv2.threshold(img,120,240,cv2.THRESH_BINARY) # 127 değeri treshold değeri olarak belirlenir.127'den küçük olan değerler 0,büyük olanlar 255 değerini alır.
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,2) #adaptive thresholding işlemi yapılır
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51,2)


cv2.imshow("Orjinal Resim",img)
cv2.imshow("Threshold Resim",th1)
cv2.imshow("Adaptive Threshold Resim",th2)
cv2.imshow("Adaptive Gaussian Threshold Resim",th3)


cv2.waitKey(0)
cv2.destroyAllWindows()