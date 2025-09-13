

" ----------------- "
# Korner Detection
" ----------------- "


import cv2
import numpy as np  

img = cv2.imread("materyal\\klasor8\\uygulamalarlaOPEnCV.png")
img2 = cv2.imread("materyal\\klasor8\\ucgenMavi.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
gray2 = np.float32(gray2)

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10) # 100 tane köşe bul, 0.01 hassasiyet, 10 mesafe
corners2 = cv2.goodFeaturesToTrack(gray2, 3, 0.01, 10) # 100 tane köşe bul, 0.01 hassasiyet, 10 mesafe

corners = np.int0(corners)
corners2 = np.int0(corners2)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img, (x,y), 3, (0,0,255), -1)

for corner in corners2:
    x,y = corner.ravel()
    cv2.circle(img2, (x,y), 3, (0,0,255), -1)

cv2.imshow("Köşeler", img)
cv2.imshow("Köşeler2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
