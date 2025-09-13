

" --------------------------- "
# GÖZ İZLEME (EYE TRACKING) 
" --------------------------- "

import cv2

vid = cv2.VideoCapture("materyal\\klasor11\\goz.mp4")

while 1:
    ret,frame=vid.read()
    if ret is False:
        break

    roi = frame[80:210,230:450] # frame[y1:y2,x1:x2]
    rows,cols,_ = roi.shape # roi.shape[0] = rows , roi.shape[1] = cols 

    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY) # Gri tonlamalı görüntü 

    _,threshold = cv2.threshold(gray,3,255,cv2.THRESH_BINARY_INV) # Gri tonlamalı görüntüyü siyah beyaz yapma

    contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # Kontürleri bulma
    contours = sorted(contours, key = lambda x: cv2.contourArea(x), reverse=True) # Kontürleri alanlarına göre sıralama

    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt) # Kontürün etrafına dikdörtgen çizme: x,y başlangıç noktası , w,h genişlik ve yükseklik
        cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2) # roi,başlangıç noktası,bitiş noktası,renk,kalınlık
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,255,0),2)
        cv2.line(roi,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)
        break
    
    frame[80:210,230:450] = roi # frame[y1:y2,x1:x2] = roi
    
    cv2.imshow("frame",frame)
  
    if cv2.waitKey(1) & 0xFF== 27: # 27 = ESC
        break

vid.release()
cv2.destroyAllWindows()