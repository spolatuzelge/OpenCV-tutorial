

#----------------------------#
# GAUSS DÜZLEŞTİRME FİLTRESİ
#----------------------------#

# Gürültülü bir resmi düzleştirmek için kullanılır.GaussianBlur fonksiyonu ile resmin üzerinde Gauss düzleştirme işlemi yapılır.


import cv2
import numpy as np

img = cv2.imread(r"materyal\woman.png") # Resmi okur.
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE) # Resim penceresi oluşturur.

h, w = img.shape[:2] # Yükseklik ve genişlik değerlerini alır.

dst = cv2.bilateralFilter(img, 0, 100, 35) # Resmi düzleştirir. 
# İlk parametre resim, ikinci parametre pikselin çapı, üçüncü ve dördüncü parametre renk ve uzaklık filtresi.


result = np.zeros([h, w*2, 3], dtype=img.dtype) # İki resmi birleştirmek için bir dizi oluşturur.
result[0:h, 0:w, :] = img # İlk resmi diziye ekler.
result[0:h, w:2*w, :] = dst # İkinci resmi diziye ekler.

cv2.imshow("Gaussian Smoothing", result) # Düzleştirilmiş resmi gösterir.
cv2.imshow("Original Image", img) # Resmi gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler.
cv2.destroyAllWindows() # Tüm pencereleri kapatır.