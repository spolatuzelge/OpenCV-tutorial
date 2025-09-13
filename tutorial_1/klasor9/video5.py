

" ----------------------------------- "
# Image Moments ve Geometrik Merkez
" ----------------------------------- "

import cv2

img = cv2.imread('materyal\\klasor9\\ucgenMavi.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Griye çevirme

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) # 127 den buyuk olanlari beyaz yapar
M = cv2.moments(thresh)  # Image Moments : Görüntü Momentleri, görüntüdeki geometrik şekillerin özelliklerini tanımlamak için kullanılır.

X = int(M["m10"]/M["m00"])
Y = int(M["m01"]/M["m00"])

cv2.circle(img,(X,Y),5,(0,255,0),-1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()