

" ---------------------------------------- "
# Bitwise Operatorler - Bit Duzeyinde Islemler
" ---------------------------------------- "

import cv2
import numpy as np

img1 =cv2.imread("materyal\\klasor8\\siyahBeyaz_tuval.png")
img2 =cv2.imread("materyal\\klasor8\\beyaz_siyahUcgen.png")

bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)


cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Bitwise AND", bitAnd)
cv2.imshow("Bitwise OR", bitOr)
cv2.imshow("Bitwise XOR", bitXor)
cv2.imshow("Bitwise NOT 1", bitNot1)
cv2.imshow("Bitwise NOT 2", bitNot2)


cv2.waitKey(0)
cv2.destroyAllWindows()