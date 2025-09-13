

" --------------------------------- "
# ROI (Region of Interest) - ilgi alanı
" --------------------------------- "

import cv2
import numpy as np

img = cv2.imread("materyal\\klasor8\\klon.jpg")


print(img.shape) # (480, 640, 3) -> 480: yukseklik, 640: genislik, 3: renk kanallari (RGB)

#### Klon askeri kafa bölgesini roi alanı olarak belirleme ####
roi = img[50:180, 240:400] # [y1:y2, x1:x2] -> y1:y2 aralığındaki satırlar, x1:x2 aralığındaki sütunlar.


cv2.imshow("ROI", roi)


cv2.imshow("Klon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
