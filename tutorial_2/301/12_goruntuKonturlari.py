

#-----------------------#
# GÖRÜNTÜ KONTURLARI
#-----------------------#

# Konturlar, nesnelerin sınırlarını ifade eden bir çizgidir. 

import cv2
import numpy as np

def tresholdDemo(x):
    dst = cv2.GaussianBlur(img, (3, 3), 0) # Gürültüyü azaltır.
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY) # Resmi gri tonlamalıya dönüştürür.
    ret , binary = cv2.threshold(gray,0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # Eşik değeri belirler.
    cv2.imshow("Binary Image", binary) # Eşiklenmiş resmi gösterir.
    cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler.
    return binary

def cannyDemo(x):
    t = 100
    cannyOutput = cv2.Canny(x, t, t*2) # Kenarları algılar.
    cv2.imshow("Canny Image", cannyOutput) # Kenarları gösterir.
    cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler
    return cannyOutput

img = cv2.imread(r"materyal\woman3.png") # Resmi okur.
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE) # Pencere oluşturur.
cv2.imshow("Original Image", img) # Resmi gösterir.

binary = tresholdDemo(img) # Eşiklenmiş resmi alır.
cannyOutput = cannyDemo(img) # Kenarları alır.

contours , hierarchy = cv2.findContours(cannyOutput, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Konturları bulur.
# İlk parametre resim, ikinci parametre kontur alma modu, üçüncü parametre kontur yaklaşım metodu.

for c in range(len(contours)):
    cv2.drawContours(img, contours, c, (0, 0, 255), 1, 8) # Konturları çizer.
    # İlk parametre resim, ikinci parametre konturlar, üçüncü parametre kontur indeksi, dördüncü parametre renk, beşinci parametre kalınlık, altıncı parametre tip.

cv2.imshow("Contours", img) # Konturlu resmi gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler.
cv2.destroyAllWindows() # Tüm pencereleri kapatır.

