

" ---------- "
# Histogram
" ---------- "

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("materyal\\klasor8\\gulenKadin.jpg")
b,g,r = cv2.split(img)

cv2.imshow("Orjinal Resim",img)
cv2.imshow("Mavi Kanal",b)
cv2.imshow("Yesil Kanal",g)
cv2.imshow("Kirmizi Kanal",r)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()