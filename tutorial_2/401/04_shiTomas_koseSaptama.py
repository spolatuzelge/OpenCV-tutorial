

#--------------------------------------#
# SHİ-TOMASİ KÖŞE SAPTAMA ALGORİTMASI
#--------------------------------------#

import cv2
import numpy as np

def ShiTomasi(img):

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Gri tonlamalı görüntüye dönüştürme işlemi
    corners = cv2.goodFeaturesToTrack(imgGray, maxCorners=35, qualityLevel=0.05,minDistance=10) # Shi-Tomasi köşe tespiti işlemi

    for i in corners:
        b = np.random.randint(0, 256) # Rastgele mavi tonu
        g = np.random.randint(0, 256) # Rastgele yeşil tonu
        r = np.random.randint(0, 256) # Rastgele kırmızı tonu
        x = np.int32(i[0][0]) # Köşenin x koordinatı
        y = np.int32(i[0][1])
        cv2.circle(img, (x, y), 3, (int(b), int(g), int(r)), -1)


    return img

img = cv2.imread(r"materyal\shiTomas.png")

copy = np.copy(img) # Resmin kopyasını alır.
copy = ShiTomasi(copy) # Shi-Tomasi köşe tespiti işlemi

result = np.concatenate((img, copy), axis=1) # Resimleri birleştirme işlemi

cv2.imshow("Shi-Tomasi Corner Detection", result) # Resmi ekranda gösterme işlemi
cv2.waitKey(0) # Bekleme işlemi
cv2.destroyAllWindows() # Pencereleri kapatma işlemi
