
#-----------------#
#  RGB -> GRAY   
#-----------------#


import cv2 

img = cv2.imread(r"materyal\logo.png")

# img = cv2.imread(r"materyal\logo.png", cv2.IMREAD_GRAYSCALE) Bu şekilde de yapılabilir.Bu durum resmi direkt olarak gri tonlamalı olarak yükler.


# Resmi gösterme
cv2.namedWindow("Logo", cv2.WINDOW_AUTOSIZE) # Pencere oluştur, cv2.WINDOW_AUTOSIZE -> Resim boyutuna göre pencere boyutunu ayarlar.
cv2.imshow("Logo", img)
cv2.waitKey()


#cvtColor() fonksiyonu ile renk dönüşümü yapılır.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # RGB -> GRAY

cv2.imshow("Logo", gray)
cv2.waitKey()


#imwrite() fonksiyonu ile resim dosyası kaydedilir.

cv2.imwrite(r"materyal\logo_gray.png", gray)
cv2.destroyAllWindows()