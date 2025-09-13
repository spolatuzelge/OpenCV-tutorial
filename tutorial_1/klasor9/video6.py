

" ------------------------------------------------------------ "
# Kontur Alanı ve Çevresi 
# [cv2.contourArea(), cv2.findContours(), cv2.drawContours()]
" ------------------------------------------------------------ "

import cv2 

img = cv2.imread("materyal\\klasor9\\ucgenMavi.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_ , thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY) # 127 den buyuk olanlari beyaz yapar
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # konturleri bulur, RETR_TREE: hiyerarsik sekilde bulur, CHAIN_APPROX_SIMPLE: cok fazla olan noktalari azaltir

cnt = contours[0]

area = cv2.contourArea(cnt) # Alan
print("Alan: ", area)

perimeter = cv2.arcLength(cnt, True) # Cevre
print("Cevre: ", perimeter)