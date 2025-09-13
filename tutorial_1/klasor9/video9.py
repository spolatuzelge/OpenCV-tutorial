

" ----------------------------------------------------------------------- "
# Convex Hull (Dışbükey Kabuk) Convexity Defects (Dışbükeylik Kusurları)
" ----------------------------------------------------------------------- "


import cv2
import numpy as np

img = cv2.imread("materyal\\klasor9\\convexHull_star.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgGray, 127, 255, 0) # 127 den buyuk olanlari beyaz yapar

contours, _ = cv2.findContours(thresh, 2,1) # konturleri bulur, RETR_TREE: hiyerarsik sekilde bulur, CHAIN_APPROX_SIMPLE: cok fazla olan noktalari azaltir

hull = cv2.convexHull(contours[0],returnPoints=0) # Dışbükey kabuk. Dışbükey kabuğun çizgilerini bulur.
defects = cv2.convexityDefects(contours[0], hull) # Dışbükeylik kusurları. Dışbükey kabuk içindeki kusurları bulur.

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0] # s: başlangıç, e: bitiş, f: uzaklık, d: mesafe
    start = tuple(contours[0][s][0]) # başlangıç
    end = tuple(contours[0][e][0]) # bitiş
    far = tuple(contours[0][f][0]) # uzaklık 
    cv2.line(img, start, end, [0, 255, 0], 2) # çizgi
    cv2.circle(img, far, 5, [0, 0, 255], -1) # daire


cv2.imshow("Image", img)
cv2.imshow("Thresh", thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()