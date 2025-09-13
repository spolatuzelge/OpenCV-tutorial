

#----------------------------------------------------#
# GÖRÜNTÜ KESKİNLEŞTİRME İŞLEMİ (IMAGE SHARPENING)
#----------------------------------------------------#

import cv2
import numpy as np

img = cv2.imread(r"materyal\person.png")

ksnk = np.array([[-1, -1, -1], [-1, 10, -1], [-1, -1, -1]], dtype=np.float32) # Keskinleştirme filtresi: 
imgKeskin = cv2.filter2D(img, cv2.CV_32F, ksnk) # Görüntü keskinleştirme işlemi : cv2.CV_32F : 32-bit float
imgSonuc = cv2.convertScaleAbs(imgKeskin) # Görüntüyü 8-bit unsigned integer türüne dönüştürme işlemi

result = np.concatenate((img, imgSonuc), axis=1) # Resimleri birleştirme işlemi

cv2.imshow("Image Sharpening", result) # Resmi ekranda gösterme işlemi
cv2.waitKey(0) # Bekleme işlemi
cv2.destroyAllWindows() # Pencereleri kapatma işlemi
