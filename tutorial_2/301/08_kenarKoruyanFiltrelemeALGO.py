

#------------------------------------------#
# KENARLARI KORUYAN FİLTRELEME ALGORİTMASI
#------------------------------------------#

# Kenarları koruyan filtreleme algoritması, kenarları koruyarak resmi düzleştirmek için kullanılır.

import cv2
import numpy as np

img = cv2.imread(r"materyal\woman.png") # Resmi okur.
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE) # Resim penceresi oluşturur.
cv2.imshow("Original Image", img) # Resmi gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler.

h, w = img.shape[:2] # Yükseklik ve genişlik değerlerini alır.

dst = cv2.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.4) # Kenarları koruyan filtreleme işlemi yapar.
# İlk parametre resim, ikinci parametre bayrak, üçüncü parametre sigma_s, dördüncü parametre sigma_r.
# sigma_s: Renk benzerliği hesaplamak için kullanılan standart sapma değeri. 0-200 arasında bir değer alır.
# sigma_r: Renk filtresi için kullanılan standart sapma değeri. 0-1 arasında bir değer alır.
# flags: 0, 1 veya 2 değerlerinden birini alır. 0: Renk ve uzaklık filtresi, 1: Renk filtresi, 2: Uzaklık filtresi.

result = np.zeros([h, w*2, 3], dtype=img.dtype) # İki resmi birleştirmek için bir dizi oluşturur.
result[0:h, 0:w, :] = img # İlk resmi diziye ekler.
result[0:h, w:2*w, :] = dst # İkinci resmi diziye ekler.

cv2.imshow("Edge Preserving Filter", result) # Kenarları koruyan filtrelenmiş resmi gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler.
cv2.destroyAllWindows() # Tüm pencereleri kapatır.
