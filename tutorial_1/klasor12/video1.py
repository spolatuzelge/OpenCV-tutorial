

" --------------------------------------- "
# Resim Karşılaştırma (Image Comparison)
" --------------------------------------- "

import cv2
import numpy as np

img1 = cv2.imread("materyal\\klasor12\\havaBalonu.jpg")
img2 = cv2.imread("materyal\\klasor12\\havaBalonu.jpg")

img1 = cv2.resize(img1, (640,480)) # Resmi yeniden boyutlandırma : (resim, (genişlik, yükseklik))
img2 = cv2.resize(img2, (640,480))


if img1.shape == img2.shape:
    print("Resimler aynı boyutlara sahip.")

    difference = cv2.subtract(img1, img2) # Resimler arasındaki farkı bulma
    b, g, r = cv2.split(difference) # Farklı pikselleri ayırma

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("Resimler aynıdır.")
    else:
        print("Resimler farklıdır.")
else:
    print("Resimler farklı boyutlara sahip.")



cv2.imshow("Hava Balonu", img1)
cv2.imshow("Hava Balonu 2", img2)
cv2.imshow("Fark", difference)
cv2.waitKey(0)
cv2.destroyAllWindows()