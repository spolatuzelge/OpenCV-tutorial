

#-----------------------#
# HOFFMAN CİZGİ TESPİTİ 
#-----------------------#

# Hoffman cizgi tespiti, resimdeki nesnelerin sınırlarını belirlemek için kullanılır.

import cv2
import numpy as np

def cannyDemo(x):
    t = 100
    cannyOutput = cv2.Canny(x, t, t*2) # Kenarları algılar.
    cv2.imshow("Canny Image", cannyOutput) # Kenarları gösterir.
    cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler
    return cannyOutput

img = cv2.imread(r"materyal\sudoku.png") # Resmi okur.
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE) # Pencere oluşturur.
cv2.imshow("Original Image", img) # Resmi gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler.

cannyOutput = cannyDemo(img) # Kenarları alır.
cv2.imshow("Canny Image", cannyOutput) # Kenarları gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler

lines = cv2.HoughLines(cannyOutput, 1, np.pi/180, 150, None, 0 ,0) # Hoffman çizgilerini bulur.
# İlk parametre resim, ikinci parametre çözünürlük, üçüncü parametre theta, dördüncü parametre eşik değeri.

if lines is not None:
    for i in range(len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1) # Çizgi çizer.
# İlk parametre resim, ikinci parametre başlangıç noktası, üçüncü parametre bitiş noktası, dördüncü parametre renk, beşinci parametre kalınlık.

cv2.imshow("Hoffman Lines", img) # Hoffman çizgilerini gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler
cv2.destroyAllWindows() # Tüm pencereleri kapatır.
