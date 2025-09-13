

#-------------------------#
# HİSTOGRAM KARŞILAŞTIRMA
#-------------------------#

import cv2

img1 = cv2.imread(r"materyal\openCV.png")      # Gri tonlamalı olarak resmi okur.
img2 = cv2.imread(r"materyal\yazi.png")        # Gri tonlamalı olarak resmi okur.
img3 = cv2.imread(r"materyal\yesillik.jpg")    # Gri tonlamalı olarak resmi okur.

img1HSV = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV) # Resmi HSV tonlamalı hale getirir.
img2HSV = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV) # Resmi HSV tonlamalı hale getirir.
img3HSV = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV) # Resmi HSV tonlamalı hale getirir.

hist1 = cv2.calcHist([img1HSV], [0, 1], None, [180, 256], [0, 180, 0, 256]) # Histogram oluşturur.
hist2 = cv2.calcHist([img2HSV], [0, 1], None, [180, 256], [0, 180, 0, 256]) # Histogram oluşturur.
hist3 = cv2.calcHist([img3HSV], [0, 1], None, [180, 256], [0, 180, 0, 256]) # Histogram oluşturur.
# cv2.calcHist([resim], [kanal], mask, [histogram boyutu], [histogram aralığı])

cv2.normalize(hist1, hist1, 0, 1, cv2.NORM_MINMAX) # Histogramı normalize eder.
cv2.normalize(hist2, hist2, 0, 1, cv2.NORM_MINMAX) # Histogramı normalize eder.
cv2.normalize(hist3, hist3, 0, 1, cv2.NORM_MINMAX) # Histogramı normalize eder.

compare1 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL) # Histogramları karşılaştırır.
compare2 = cv2.compareHist(hist1, hist3, cv2.HISTCMP_CORREL) # Histogramları karşılaştırır.
compare3 = cv2.compareHist(hist2, hist3, cv2.HISTCMP_CORREL) # Histogramları karşılaştırır.

print("OpenCV ve Yazi resimlerinin benzerlik oranı: ", compare1)
print("OpenCV ve Yesillik resimlerinin benzerlik oranı: ", compare2)
print("Yazi ve Yesillik resimlerinin benzerlik oranı: ", compare3)

cv2.imshow("OpenCV", img1)
cv2.imshow("Yazi", img2)
cv2.imshow("Yesillik", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()