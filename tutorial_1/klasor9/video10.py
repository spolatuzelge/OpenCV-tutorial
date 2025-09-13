

" ----------------------------------------------------------------------- "
# Convex Hull (Dışbükey Kabuk) Convexity Defects (Dışbükeylik Kusurları)
" ----------------------------------------------------------------------- "

import cv2
import numpy as np

img = cv2.imread(r"materyal\klasor9\convexHull_map.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Griye çevirme
blur = cv2.blur(gray,(3,3)) # Bulanıklaştırma
ret,thresh = cv2.threshold(blur,40,255,cv2.THRESH_BINARY) # Eşikleme

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # Konturları bulma

hull = [] # Dışbükey kabuk

for i in range(len(contours)): # Konturların sayısı kadar döngü
    hull.append(cv2.convexHull(contours[i],False)) # Dışbükey kabukları bulma

bg = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8) # Arka plan

for i in range(len(contours)): # Konturların sayısı kadar döngü
    cv2.drawContours(bg,contours,i,(255,0,0),3,8) # Konturları çizme
    cv2.drawContours(bg,hull,i,(0,255,0),1,8) # Dışbükey kabukları çizme


cv2.imshow("Image",bg) # Arka planı gösterme


cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh = cv2.threshold()