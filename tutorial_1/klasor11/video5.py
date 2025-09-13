

" -------------------------------------------- "
# Arka Plan Çıkarma (Background Subtraction) 
" -------------------------------------------- "

import cv2
import numpy as np

cap = cv2.VideoCapture("materyal\\klasor11\\car_HighWay.mp4") # Videoyu açma

subtractor = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=120,detectShadows=True)
# createBackgroundSubtractorMOG2 : Arka plan çıkarma algoritması oluşturur
# history : Arka plan modelinin geçmiş kare sayısı
# varThreshold : Arka plan modelinin varyans eşiği
# detectShadows : Gölge algılama

while 1:
    _,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    mask = subtractor.apply(frame)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
