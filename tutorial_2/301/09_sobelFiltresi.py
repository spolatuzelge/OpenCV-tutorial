

#----------------#
# SOBEL FİLTRESİ
#----------------#

# Sobel filtresi, kenar tespiti için kullanılır. Sobel filtresi, x ve y yönlerinde türev alarak kenarları tespit eder.

import cv2
import numpy as np

img = cv2.imread(r"materyal\openCV.png") # Resmi okur.

h, w = img.shape[:2] # Yükseklik ve genişlik değerlerini alır.

xGrad = cv2.Sobel(img, cv2.CV_32F, 1, 0) # X yönünde türev alır.
yGrad = cv2.Sobel(img, cv2.CV_32F, 0, 1) # Y yönünde türev alır.

xGrad = cv2.convertScaleAbs(xGrad) # X türevini mutlak değere dönüştürür.
yGrad = cv2.convertScaleAbs(yGrad) # Y türevini mutlak değere dönüştürür.

result = np.zeros([h, w*2, 3], dtype=img.dtype) # İki resmi birleştirmek için bir dizi oluşturur.
result[0:h, 0:w, :] = xGrad # İlk resmi diziye ekler.
result[0:h, w:2*w, :] = yGrad # İkinci resmi diziye ekler.

dst = cv2.addWeighted(xGrad, 0.5, yGrad, 0.5, 0) # İki resmi birleştirir.


cv2.imshow("Sobel Edge Detection", result) # Kenarları tespit edilmiş resmi gösterir.
cv2.imshow("Sobel Edge Detection2", dst) # Kenarları tespit edilmiş resmi gösterir.
cv2.imshow("Original", img) # Orijinal resmi gösterir.
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler.
cv2.destroyAllWindows() # Tüm pencereleri
