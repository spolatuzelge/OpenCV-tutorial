

" -------------------------------------- "
# Resim Dönüşümü (Image Transformation)
" -------------------------------------- "

import cv2
import numpy as np

def nothing(x):
    pass


imgHavaBalonu = cv2.imread("materyal\\klasor12\\havabalonu.jpg") # Ana Görüntü
imgBaloon = cv2.imread("materyal\\klasor12\\baloon.jpg") # Şablon Görüntü

imgHavaBalonu = cv2.resize(imgHavaBalonu, (640, 480)) # Görüntüyü Yeniden Boyutlandırma
imgBaloon = cv2.resize(imgBaloon, (640, 480))

output = cv2.addWeighted(imgHavaBalonu, 0.5, imgBaloon, 0.5, 0) 
# addWeighted: İki Görüntüyü Birleştirme İşlemi : (Görüntü1, Ağırlık1, Görüntü2, Ağırlık2, Beta)
cv2.namedWindow("Output") # Pencere Oluşturma
cv2.createTrackbar("Alpha - Beta", "Output", 0, 1000, nothing) # Alpha Değeri

while True:
    cv2.imshow("Output", output) # Görüntüyü Gösterme
    alpha = cv2.getTrackbarPos("Alpha - Beta", "Output") / 1000 # Alpha Değerini Al
    beta = 1 - alpha # Beta Değerini Al
    output = cv2.addWeighted(imgHavaBalonu, alpha, imgBaloon, beta, 0) # Görüntü Birleştirme İşlemi

    if cv2.waitKey(1) & 0xFF == ord("q"): # Çıkış İşlemi
        break

cv2.destroyAllWindows() # Pencereleri Kapatma