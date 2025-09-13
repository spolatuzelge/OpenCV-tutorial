

" ----------------------------------------------------- "
# Renk Uzayı Nedir, Görüntülerin Renk Uzayı Dönüşümleri
# [cv.cvtColor() ,
" ----------------------------------------------------- "

import cv2
import numpy as np

img = cv2.imread("materyal\\klasor8\\klon.jpg")
imgERGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR -> RGB
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   # BGR -> HSV
imgGRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR -> GRAY


cv2.imshow("Orjinal", img)
cv2.imshow("RGB", imgERGB)
cv2.imshow("HSV", imgHSV)
cv2.imshow("GRAY", imgGRAY)

cv2.waitKey(0)
cv2.destroyAllWindows()