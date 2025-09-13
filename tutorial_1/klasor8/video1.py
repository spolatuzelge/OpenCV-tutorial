

" --------------------------------- "
# Pikseller
" --------------------------------- "

import cv2
import numpy as np

img = cv2.imread("materyal\\klasor8\\klon.jpg")

"""dimension = img.shape
print(dimension)"""

"""color = img[150, 200]
print(color)"""


#### İstenilen pikselin rengini almak icin ####

blue = img[150, 200, 0] # 0: mavi, 1: yesil, 2: kirmizi. (150,200) pikselinin mavi degerini alir.
green = img[150, 200, 1]
red = img[150, 200, 2]

print("blue : ",blue)
print("green : ",green)
print("red : ",red)

###############################


#### İstenilen pikselin rengini degistirmek icin ####

img[150, 200] = [255, 255, 255] # (150,200) pikselinin rengini beyaz yapar.
#######################################################





cv2.imshow("Klon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()