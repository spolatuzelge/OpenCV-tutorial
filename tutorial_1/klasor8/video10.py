

" ---------------------------------------- "
# Resim Dönüşüm Dizeyi (Matrix)
" ---------------------------------------- "

import cv2
import numpy as np

img= cv2.imread("materyal\\klasor8\\helikopter.png",0)

row , col = img.shape

# Dönüşüm Matrisi
M= np.float32([[1,0,100],[0,1,250]]) # Girilen değerler x ve y ekseninde kaydırma yapar.

dst= cv2.warpAffine(img,M,(col,row))

cv2.imshow("Orjinal Resim",img)
cv2.imshow("Dönüşüm Resmi",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()