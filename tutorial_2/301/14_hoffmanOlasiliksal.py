

#------------------------------------#
# HOFFMAN OLASILIKSAL CİZGİ TESPİTİ 
#------------------------------------#

# Hoffman olasılıksal çizgi tespiti, resimdeki nesnelerin sınırlarını belirlemek için kullanılır.
# Bu yöntem, resimdeki kenarları algılar ve kenarların birleşiminden oluşan çizgileri belirler.

import cv2
import numpy as np

def cannyDemo(x):
    t = 100
    cannyOutput = cv2.Canny(x, t, t*2) # Kenarları algılar.
    cv2.imshow("Canny Image", cannyOutput) # Kenarları gösterir.
    cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler
    return cannyOutput

img = cv2.imread(r"materyal\onDort.png") # Resmi okur.
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE) # Pencere oluşturur.
cv2.imshow("Original Image", img) # Resmi gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler.

cannyOutput = cannyDemo(img) # Kenarları alır.
cv2.imshow("Canny Image", cannyOutput) # Kenarları gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler

lines = cv2.HoughLinesP(cannyOutput, 1, np.pi/180, 55, None, 50, 10) # Hoffman olasılıksal çizgilerini bulur.
# İlk parametre resim, ikinci parametre çözünürlük, üçüncü parametre theta, dördüncü parametre eşik değeri.
# Beşinci parametre minLineLength, altıncı parametre maxLineGap.

if lines is not None:
    for i in range(len(lines)):
        x1, y1, x2, y2 = lines[i][0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1) # Çizgi çizer.

cv2.imshow("Hoffman Probabilistic Lines", img) # Hoffman olasılıksal çizgilerini gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler
cv2.destroyAllWindows() # Tüm pencereleri kapatır.
