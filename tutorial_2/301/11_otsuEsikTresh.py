

#-----------------------#
# OTSU EŞİKLEME YÖNTEMİ 
#-----------------------#

# Otsu eşikleme yöntemi, resimdeki nesne ve arka planı ayırmak için kullanılır. 
# Bu yöntem, resimdeki piksel değerlerini iki gruba ayırır. 
# Bu iki grup arasındaki varyansı maksimize eder ve eşik değerini belirler.
# Otsu eşikleme yöntemi, gri tonlamalı resimlerde kullanılır.

import cv2
import numpy as np

img = cv2.imread(r"materyal\woman2.png", 0) # Resmi okur.
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE) # Pencere oluşturur.
cv2.imshow("Original Image", img) # Resmi gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler.

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # Eşik değeri belirler.
# İlk parametre resim, ikinci parametre eşik değeri, üçüncü parametre maksimum değer, dördüncü parametre eşikleme yöntemi.

h, w = img.shape[:2] # Yükseklik ve genişlik değerlerini alır.
print("Threshold value: ", ret) # Eşik değerini yazdırır.

cv2.imshow("Otsu Thresholding", th1) # Eşiklenmiş resmi gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler.
cv2.destroyAllWindows() # Tüm pencereleri
