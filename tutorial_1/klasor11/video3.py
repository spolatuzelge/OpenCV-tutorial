

" ------------------------------------------------------------- "
# Gerçek Zamanlı Çokgen Algılama (Real Time Shape Detection )
" ------------------------------------------------------------- "

import cv2
import numpy as np


def nothing(x):
    pass

vid = cv2.VideoCapture(0) # Kamera açma
font = cv2.FONT_HERSHEY_SIMPLEX # Font tipi belirleme

cv2.namedWindow("Trackbar") # Trackbar oluşturma

cv2.createTrackbar("L - H", "Trackbar", 0, 179, nothing) # Trackbar oluşturma
cv2.createTrackbar("L - S", "Trackbar", 0, 255, nothing) 
cv2.createTrackbar("L - V", "Trackbar", 0, 255, nothing) 
cv2.createTrackbar("U - H", "Trackbar", 179, 179, nothing) 
cv2.createTrackbar("U - S", "Trackbar", 255, 255, nothing) 
cv2.createTrackbar("U - V", "Trackbar", 255, 255, nothing) 

while True :
    ret, frame = vid.read() # Kameradan görüntü alır
    frame = cv2.flip(frame, 1) # Görüntüyü çevirir

    lowerHue = cv2.getTrackbarPos("L - H", "Trackbar") # Trackbar değerini alır
    lowerSaturation = cv2.getTrackbarPos("L - S", "Trackbar") 
    lowerValue = cv2.getTrackbarPos("L - V", "Trackbar") 
    upperHue = cv2.getTrackbarPos("U - H", "Trackbar") 
    upperSaturation = cv2.getTrackbarPos("U - S", "Trackbar") 
    upperValue = cv2.getTrackbarPos("U - V", "Trackbar") 

    loweColor = np.array([lowerHue, lowerSaturation, lowerValue]) # Renk aralığını belirler
    upperColor = np.array([upperHue, upperSaturation, upperValue]) # Renk aralığını belirler

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Renk uzayını değiştirir
    mask = cv2.inRange(hsv, loweColor, upperColor) # Renk aralığını belirler
    kernel = np.ones((5, 5), np.uint8) # Çekirdek oluşturur
    mask = cv2.erode(mask, kernel) # Erozyon işlemi uygular

    countours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Çizgileri bulur

    for cnt in countours :
        area = cv2.contourArea(cnt) # Alanı belirler
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)

        cv2.drawContours(frame, [approx], 0, (0, 0, 0), 2)

        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400 :
            if len(approx) == 3 :
                cv2.putText(frame, "Ucgen", (x, y), font, 1, (0, 0, 0))
            elif len(approx) == 4 :
                cv2.putText(frame, "Dortgen", (x, y), font, 1, (0, 0, 0))
            elif len(approx) == 5 :
                cv2.putText(frame, "Besgen", (x, y), font, 1, (0, 0, 0))
            elif len(approx) > 6 :
                cv2.putText(frame, "Altigen", (x, y), font, 1, (0, 0, 0))

    cv2.imshow("Gerçek Zamanlı Çokgen Algılama", frame)
    cv2.imshow("Maske", mask)
    
    if cv2.waitKey(1) & 0xFF == ord("q") :
        break

vid.release()
cv2.destroyAllWindows()
