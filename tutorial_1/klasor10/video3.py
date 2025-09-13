

" --------------------------------------------------------- "
# Hough Line Transform (Hough Doğru Dönüşümü) - Resimlerde
" --------------------------------------------------------- "

import cv2
import numpy as np

img = cv2.imread("materyal\\klasor10\\hougLine.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Griye çevirme
edges = cv2.Canny(gray,50,150,apertureSize = 3) 
# Köşeleri bulma (Canny) ; 50 ve 150 değerleri arasındaki kenarları bulma. apertureSize = 3 ise kenarları bulma işleminin çözünürlüğüdür.

lines = cv2.HoughLinesP(edges,1,np.pi/180,30,maxLineGap=250) 
# Hough Doğru Dönüşümü ; 1 ve np.pi/180 değerleri arasındaki doğruları bulma. 30 ise doğru olma eşiğidir. 250 ise doğrular arasındaki boşluktur.

for line in lines:
    x1 , y1 , x2 , y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2) # Doğruları çizme
    

cv2.imshow("Image",img) # Resmi gösterme
cv2.imshow("Gray",gray) # Gri tonlam gösterme
cv2.imshow("Edges",edges) # Köşeleri gösterme
cv2.waitKey(0)
cv2.destroyAllWindows()