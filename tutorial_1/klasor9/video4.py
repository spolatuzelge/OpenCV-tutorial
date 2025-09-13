

" ----------------------------------- "
# Nesnelerin İzini Sürme (Beyaz Renk)
" ----------------------------------- "

import cv2
import numpy as np

cap = cv2.VideoCapture("materyal\\klasor9\\dog.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Hue, Saturation, Value : Renk, Doygunluk, Parlaklık. Renklerin tanımlanmasında kullanılır.

    lower_blue = np.array([0, 0, 240]) 
    upper_blue = np.array([255, 15, 255]) 
    mask = cv2.inRange(hsv, lower_blue, upper_blue) # Belirtilen aralıktaki renkleri beyaz yapar, diğerlerini siyah yapar.

    res = cv2.bitwise_and(frame, frame, mask = mask) #cv2.bitwise_and: iki resmi birleştirir. mask: hangi rengin alınacağını belirler. 

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()