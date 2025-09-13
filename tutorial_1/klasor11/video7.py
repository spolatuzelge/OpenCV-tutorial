

" ----------------------- "
# HSV İLE NESNE SAPTAMA  
" ----------------------- "

import cv2
import numpy as np

def nothing(x): # Trackbar fonksiyonu : Hiçbir şey yapma (pass)
    pass

cap = cv2.VideoCapture("materyal\\klasor11\\silgi.mp4") # Videoyu açma

cv2.namedWindow("Trackbars") # Trackbar penceresi oluşturma
cv2.createTrackbar("Low Hue","Trackbars",0,179,nothing) # Trackbar oluşturma
cv2.createTrackbar("Low Saturation","Trackbars",0,255,nothing)
cv2.createTrackbar("Low Value","Trackbars",0,255,nothing)
cv2.createTrackbar("High Hue","Trackbars",0,179,nothing)
cv2.createTrackbar("High Saturation","Trackbars",0,255,nothing)
cv2.createTrackbar("High Value","Trackbars",0,255,nothing)

while 1:
    _,frame=cap.read()

    if _ is False: 
        continue 
    
    frame=cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lHue = cv2.getTrackbarPos("Low Hue","Trackbars") # Trackbar değerlerini al
    lSaturation = cv2.getTrackbarPos("Low Saturation","Trackbars") 
    lValue = cv2.getTrackbarPos("Low Value","Trackbars")
    hHue = cv2.getTrackbarPos("High Hue","Trackbars")
    hSaturation = cv2.getTrackbarPos("High Saturation","Trackbars")
    hValue = cv2.getTrackbarPos("High Value","Trackbars")

    lower = np.array([lHue,lSaturation,lValue])
    upper = np.array([hHue,hSaturation,hValue])

    mask = cv2.inRange(hsv,lower,upper) # HSV renk aralığına göre maskeleme işlemi
    bitwise = cv2.bitwise_and(frame,frame,mask=mask) # Maskeleme işlemi

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("bitwise",bitwise)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()