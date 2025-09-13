

#--------------------------------------#
# SUBPIXEL KÖŞE SAPTAMA ALGORİTMASI
#--------------------------------------#

import cv2
import numpy as np

def SubPixel(img):

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Gri tonlamalı görüntüye dönüştürme işlemi
    corners = cv2.goodFeaturesToTrack(imgGray, maxCorners=100, qualityLevel=0.05,minDistance=10) # Shi-Tomasi köşe tespiti işlemi

    for i in corners:
        b = np.random.randint(0, 256) # Rastgele mavi renk değeri 
        g = np.random.randint(0, 256) # Rastgele yeşil renk değeri
        r = np.random.randint(0, 256) # Rastgele kırmızı renk değeri

        x = np.int32(i[0][0]) # Köşe koordinatları "x" değeri
        y = np.int32(i[0][1]) # Köşe koordinatları "y" değeri

        cv2.circle(img, (x, y), 3, (int(b), int(g), int(r)), -1) # Daire çizme işlemi

    winSize = (5, 5)  # Arama penceresi boyutu
    zeroZone = (-1, -1) # Sıfır bölgesi
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, 0.001) # Kriterler belirlenir
    corners = cv2.cornerSubPix(imgGray, corners, winSize, zeroZone, criteria) # Subpixel köşe tespiti işlemi
    # cornerSubPix(resim, köşeler, winSize, zeroZone, criteria)

    return img

img = cv2.imread(r"materyal\shiTomas.png") # Resmi okuma işlemi

copy = np.copy(img) # Resmin kopyasını alır.
copy = SubPixel(copy) # Subpixel köşe tespiti işlemi

result = np.concatenate((img, copy), axis=1) # Resimleri birleştirme işlemi

cv2.imshow("SubPixel Corner Detection", result) # Resmi ekranda gösterme işlemi
cv2.waitKey(0) # Bekleme işlemi
cv2.destroyAllWindows() # Pencereleri kapatma işlemi
