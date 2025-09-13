

" --------------------------------- "
# Pencereyi Yeniden Boyutlandırma 
# [cv2.resize()]
" --------------------------------- "

import cv2

cv2.namedWindow("Klon", cv2.WINDOW_NORMAL)
img = cv2.imread("materyal\\klasor6\\klon.jpg")
img = cv2.resize(img, (640, 480))

cv2.imshow("Klon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()