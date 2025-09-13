

" ------------------------------------------------------------ "
# Convex Hull (Dışbükey Kabuk)
" ------------------------------------------------------------ "


import cv2
import numpy as np

img = cv2.imread("materyal\\klasor9\\convexHull_map.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(imgGray, (3,3))

_, thresh = cv2.threshold(blur, 40, 255, cv2.THRESH_BINARY)

contours,hiyerarsi = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
hull = []

for i in range(len(contours)): 
    hull.append(cv2.convexHull(contours[i], False)) 

background = np.zeros((thresh.shape[0], thresh.shape[1], 3), dtype=np.uint8)

for i in range(len(contours)):
    cv2.drawContours(background, contours, i, (255, 0, 0), 3, 8)
    cv2.drawContours(background, hull, i, (0, 255, 0), 3, 8)
    
cv2.imshow("Image", background)

cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()