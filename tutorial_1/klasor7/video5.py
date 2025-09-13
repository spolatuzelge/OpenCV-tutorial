

" --------------------------------- "
# Yazı Yazdırma
" --------------------------------- "

import cv2
import numpy as np

tuval = np.zeros((512, 512, 3), dtype="uint8") + 255

cv2.putText(tuval, "Merhaba Dunya", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2) 
# parametreler: tuval, yazı, konum, font, boyut, renk, kalınlık

cv2.putText(tuval, "Merhaba Dunya", (100,200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0,0,0), 2)

cv2.imshow("Tuval", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()