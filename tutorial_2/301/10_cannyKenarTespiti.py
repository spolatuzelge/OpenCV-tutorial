

#----------------------#
# CANNY KENAR TESPİTİ 
#----------------------#

# Canny kenar tespiti, kenarları tespit etmek için kullanılır. Canny kenar tespiti, 5 adımdan oluşur:
# 1. Gürültüyü azaltma
# 2. Görüntü gradyanlarını bulma
# 3. Non-maximum suppression
# 4. Kenarları belirleme
# 5. Kenarları bağlama

import cv2
import numpy as np

img = cv2.imread(r"materyal\man.png")
cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Original Image", img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Resmi gri tonlamalıya dönüştürür.

edges = cv2.Canny(img, 80, 250) # Canny kenar tespiti işlemi yapar.
# İlk parametre resim, ikinci parametre eşik değeri 1, üçüncü parametre eşik değeri 2.

cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()