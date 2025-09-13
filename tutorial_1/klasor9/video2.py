

" ---------- "
# Konturler
" ---------- "

import cv2
import numpy as np


img = cv2.imread("materyal\\klasor9\\video2Kontur.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_ , thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY) # 127 den buyuk olanlari beyaz yapar
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # konturleri bulur, RETR_TREE: hiyerarsik sekilde bulur, CHAIN_APPROX_SIMPLE: cok fazla olan noktalari azaltir
# print("Kontur Değerleri: ", contours) # Kontur Değerleri:  [array([[[  0,   0]], [[  0, 499]], [[499, 499]], [[499,   0]]], dtype=int32)]

cv2.drawContours(img, contours, -1, (0, 255, 0), 3) # -1: tum konturleri cizer, 3: kalinlik

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

