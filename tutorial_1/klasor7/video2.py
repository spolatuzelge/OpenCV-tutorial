

" --------------------------------- "
# Çizim Ekranı Oluşturma
" --------------------------------- "

import cv2
import numpy as np

tuval = np.zeros((512, 512, 3), dtype="uint8") # np.zeros ile 512x512 boyutunda siyah bir ekran oluşturduk.
#print(tuval) ---> bgr : 0,0,0 ==> siyah ; 0,0,255 ==> kırmızı ; 0,255,0 ==> mavi ; 255,0,0 ==> yeşil ; 255,255,255 ==> beyaz

tuval = tuval + 255 # tuval matrisine 255 ekleyerek beyaz bir ekran oluşturduk.


cv2.imshow("Tuval", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()