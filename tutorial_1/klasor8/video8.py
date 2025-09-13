

" ---------------------------------------- "
# Smoothing (Düzleştirme - Gürültü Azaltma)
" ---------------------------------------- "

import cv2
import numpy as np

imgFilter = cv2.imread("materyal\\klasor8\\openCV_filter.png")
imgMedian = cv2.imread("materyal\\klasor8\\openCV_median.png")
imgBiteral = cv2.imread("materyal\\klasor8\\kahverengiGorsel.png")

blur = cv2.blur(imgFilter, (21, 21)) # (pozitif_tekSayi,pozitif_tekSayi) 
gaussian = cv2.GaussianBlur(imgFilter, (21, 21), 0) # parametreler: (resim, pixel_capi, standart_sapma), standart_sapma=0 ise otomatik hesaplanır
median = cv2.medianBlur(imgMedian, 21) # parametreler: (resim, pixel_capi)
biteral = cv2.bilateralFilter(imgBiteral, 21, 105, 105) # parametreler: (resim, pixel_capi, renk_alan_capi, uzaklik_alan_capi)

cv2.imshow("Original Filter", imgFilter)
cv2.imshow("Original Median", imgMedian)
cv2.imshow("Original Biteral", imgBiteral)
cv2.imshow("Blur", blur)
cv2.imshow("Gaussian", gaussian)
cv2.imshow("Median", median)
cv2.imshow("Biteral", biteral)

cv2.waitKey(0)
cv2.destroyAllWindows()