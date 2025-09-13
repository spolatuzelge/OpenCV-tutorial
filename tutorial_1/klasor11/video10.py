

" ------------------------------ "
# FARE KULLANIMI (MOUSE EVENTS)
# mouse'a basıldığında , imleçin bulunduğu konumda bir daire çizilmesi
" ------------------------------ "

import cv2
import numpy as np

cap = cv2.VideoCapture(0) # Videoyu açma

circles = [] # Dairelerin konumlarını tutacak liste
def event(event,x,y,flags,param): # Event fonksiyonu
    if event == cv2.EVENT_LBUTTONDOWN: # Eğer fareye tıklandıysa
        circles.append((x,y))



cv2.namedWindow("frame") # Pencere oluşturma
cv2.setMouseCallback("frame",event) # Fare olaylarını algılama

while 1:
    _,frame=cap.read()
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(640,480))

    if _ is False: 
        continue 
    
    for center in circles:
        cv2.circle(frame,center,100,(255,0,0),-1)
    cv2.imshow("frame",frame)

    key = cv2.waitKey(1) 

    if key == 27: # ESC tuşuna basıldığında
        break
    elif key == ord('c'): # 'c' tuşuna basıldığında
        circles = [] # Dairelerin listesini temizle

cap.release()
cv2.destroyAllWindows() # Pencereleri kapat
