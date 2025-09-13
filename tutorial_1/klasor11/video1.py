

" ------------------------------------- "
# Çokgen Algılama ( Shape Detection )
" ------------------------------------- "

import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX # Font tipi belirleme

img = cv2.imread("materyal\\klasor11\\poligon.png") 
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Gri tonlamalı hale getirir 
_,treholdImg = cv2.threshold(grayImg, 240, 255, cv2.THRESH_BINARY) # 240 ve 255 arasındaki değerleri beyaz yapar

countours, _ = cv2.findContours(treholdImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Çizgileri bulur

for cnt in countours :
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True) # Çizgileri yaklaşık olarak çizer
    # 0.01*cv2.arcLength(cnt, True) : Çizgilerin uzunluğunu belirler

    cv2.drawContours(img, [approx], 0, (0, 0, 0), 2) # Çizgileri çizer, 0. çizgiyi belirler, 2 çizginin kalınlığını belirler

    x = approx.ravel()[0] # x koordinatı
    y = approx.ravel()[1] # y koordinatı

    if len(approx) == 3 : # Çokgenin kenar sayısına göre şekil belirleme
        cv2.putText(img, "Ucgen", (x, y), font, 1, (0, 0, 0))
    elif len(approx) == 4 : 
        cv2.putText(img, "Dortgen", (x, y), font, 1, (0, 0, 0))
    elif len(approx) == 5 :
        cv2.putText(img, "Besgen", (x, y), font, 1, (0, 0, 0))
    elif len(approx) == 6 :
        cv2.putText(img, "Altigen", (x, y), font, 1, (0, 0, 0))
    else :
        cv2.putText(img, "Elips", (x, y), font, 1, (0, 0, 0))


cv2.imshow("Çokgen Algılama", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
