

" --------------------------------- "
# Çizim Fonksiyonları
" --------------------------------- "

import cv2
import numpy as np

tuval = np.zeros((512, 512, 3), dtype="uint8") + 255

cv2.line(tuval, (0,0), (512,512), (0,255,0), 3) # (0,0) ve (512,512) noktaları arasında 3 kalınlığında yeşil bir çizgi çizdik.
cv2.line(tuval, (0,512), (512,0), (255,0,0), 3) 

cv2.rectangle(tuval, (100,100), (250,250), (0,0,255), 3) 

cv2.circle(tuval, (300,300), 50, (255,255,0), 3) # 50 yarıçapında mavi bir daire çizdik.


############### ÜÇGEN ÇİZİMİ ###############
p1 = (100, 400)
p2 = (250, 400)
p3 = (175, 250)

cv2.line(tuval, p1, p2, (0,0,0), 3)
cv2.line(tuval, p2, p3, (0,0,0), 3)
cv2.line(tuval, p1, p3, (0,0,0), 3)
############################################


cv2.imshow("Tuval", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()