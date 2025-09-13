
#-----------------#
# Resim Yükleme
#-----------------#

import cv2

# Resim yükleme
img = cv2.imread(r"materyal\logo.png") # Resmi oku

# Resmi gösterme
cv2.namedWindow("Logo") # Pencere oluştur
cv2.imshow("Logo", img) # Resmi göster
cv2.waitKey(0)
cv2.destroyAllWindows()