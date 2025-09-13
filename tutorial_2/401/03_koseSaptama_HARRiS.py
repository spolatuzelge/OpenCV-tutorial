

#----------------------------------#
# HARRİS KÖŞE SAPTAMA ALGORİTMASI 
#----------------------------------#

import cv2
import numpy as np

def Harris(x):
    blockSize = 2 # Kare boyutu
    apertureSize = 3 # Sobel gradyanı için
    k = 0.04 # Harris detektörü için serbest parametre

    imgGray = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY) # Gri tonlamalı görüntüye dönüştürme işlemi
    dst = cv2.cornerHarris(imgGray, blockSize, apertureSize, k) # Harris köşe tespiti işlemi
    dstNorm = np.empty(dst.shape, dtype=np.float32) # Boş bir dizi oluşturma işlemi
    dstNorm = cv2.normalize(dst, dstNorm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX) # Normalleştirme işlemi

    for i in range(dstNorm.shape[0]):
        for j in range(dstNorm.shape[1]):
            if int(dstNorm[i, j]) > 150: # Eşik değeri
                cv2.circle(x, (j, i), 3, (0, 255, 0), -1) # Daire çizme işlemi

    return x

img = cv2.imread(r"materyal\satranc.png" )

copy = np.copy(img) # Resmin kopyasını alır.

copy = Harris(copy) # Harris köşe tespiti işlemi

result = np.concatenate((img, copy), axis=1) # Resimleri birleştirme işlemi

cv2.imshow("Harris Corner Detection", result) # Resmi ekranda gösterme işlemi
cv2.waitKey(0) # Bekleme işlemi
cv2.destroyAllWindows() # Pencereleri kapatma işlemi
