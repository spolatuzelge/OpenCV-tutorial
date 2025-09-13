

" ----------------------------------------------- "
# Bulanık Görüntü Saptama (Blur Image Detection)
# cv2.Laplacian
" ----------------------------------------------- "

import cv2
import numpy as np

img = cv2.imread("materyal\\klasor12\\klon.jpg")
blurImg = cv2.medianBlur(img, 11) # Görüntüyü bulanıklaştırma

imgs = [img, blurImg]

for detec in imgs:
    laplacian = cv2.Laplacian(detec, cv2.CV_64F).var()
    
    if laplacian < 500:
        print("Bulanık Görüntü : " , laplacian)
    else:
        print("Normal Görüntü : ", laplacian)



cv2.imshow("Klon", img)
cv2.imshow("Klon Bulanık", blurImg)
cv2.waitKey(0)
cv2.destroyAllWindows()