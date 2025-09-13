

" -------------------------------------- "
# Şablon Eşleştirme (Template Matching)
" -------------------------------------- "

import cv2
import numpy as np

img = cv2.imread("materyal\\klasor12\\klon.jpg") # Ana Görüntü
img2 = cv2.imread("materyal\\klasor12\\klon2.jpg") # Şablon Görüntü 

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Ana Görüntüyü Griye Çevirme
img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) # Şablon Görüntüyü Griye Çevirme

result = cv2.matchTemplate(imgGray, img2Gray, cv2.TM_CCOEFF_NORMED) # Eşleştirme İşlemi
# cv2.TM_CCOEFF_NORMED: Kullanılan Eşleştirme Yöntemi 

loc = np.where(result >= 0.95) # Eşleşen Sonuçları Belirleme
# 0.7: Eşleşme Oranı

for point in zip(*loc[::-1]): # Eşleşen Sonuçları Döngüye Almak
    print("Point : ",point) # Eşleşen Sonuçları Yazdırma
    cv2.rectangle(img, point, (point[0] + img2.shape[1], point[1] + img2.shape[0]), (0, 255, 255), 2) # Eşleşen Sonuçları Çerçeveleme

print("Location : ",loc) # Eşleşen Sonuçları Yazdırma
print("Result : ",result) # Sonuçları Yazdırma

cv2.imshow("Klon", img)
cv2.imshow("Klon2", img2)
cv2.imshow("Sonuç", result)
cv2.waitKey(0)
cv2.destroyAllWindows() 