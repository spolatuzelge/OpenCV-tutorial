

" --------------------------- "
# YÜZ ÖZELLİKLERİNİ KULLANMA 
" --------------------------- "

import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0) # Videoyu açma

def maksContour(contours): # En büyük kontürü seçme
    max_i = 0
    max_area = 0
    for i in range(len(contours)):
        areaFace = cv2.contourArea(contours[i])
        if areaFace > max_area:
            max_area = areaFace
            max_i = i
        try :
            c = contours[max_i]
            return c
        except:
            contours = [0]
            c = contours[0]
    return c


while 1:
    ret , frame = cap.read()
    frame = cv2.flip(frame,1)

    roi = frame[180:350,200:400] # Yüz bölgesini seçme [y1:y2,x1:x2]

    cv2.rectangle(frame,(200,180),(400,350),(0,255,0),0) # Yüz bölgesini çerçeve içine alma (frame,başlangıç noktası,bitiş noktası,renk,kalınlık)

    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV) # HSV dönüşümü
    lowerColor = np.array([0,50,20],np.uint8) # Alt sınır
    upperColor = np.array([100,255,255],np.uint8) # Üst sınır


    mask = cv2.inRange(hsv,lowerColor,upperColor) # HSV renk aralığına göre maskeleme işlemi
    kernel = np.ones((3,3),np.uint8) # 5x5 boyutunda bir matris oluştur
    mask = cv2.dilate(mask,kernel,iterations=1) # Maskeleme işlemi
    mask = cv2.medianBlur(mask,15) # Maskeleme işlemi

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # Kontür bulma

    if len(contours) > 0:

        c = maksContour(contours)
        
        enSag = tuple(c[c[:,:,0].argmax()][0]) # En sağdaki nokta
        enSol = tuple(c[c[:,:,0].argmin()][0]) # En soldaki nokta
        enUst = tuple(c[c[:,:,1].argmin()][0]) # En üstteki nokta
        enAlt = tuple(c[c[:,:,1].argmax()][0]) # En alttaki nokta

        cv2.circle(roi,enSag,5,[255,0,0],-1) # En sağdaki noktayı işaretleme
        cv2.circle(roi,enSol,5,[255,0,0],-1) # En soldaki noktayı işaretleme
        cv2.circle(roi,enUst,5,[255,0,0],-1) # En üstteki noktayı işaretleme
        cv2.circle(roi,enAlt,5,[255,0,0],-1) # En alttaki noktayı işaretleme

        cv2.line(roi,enSag,enUst,(0,255,0),2)
        cv2.line(roi,enUst,enSol,(0,255,0),2)
        cv2.line(roi,enSol,enAlt,(0,255,0),2)
        cv2.line(roi,enAlt,enSag,(0,255,0),2)
        
        a=math.sqrt((enSag[0]-enUst[0])**2 + (enSag[1]-enUst[1])**2)
        b=math.sqrt((enAlt[0]-enSag[0])**2 + (enAlt[1]-enSag[1])**2)
        c=math.sqrt((enAlt[0]-enUst[0])**2 + (enAlt[1]-enUst[1])**2)
        try:
            angle = math.acos((a**2 + b**2 - c**2)/(a*b*c))*57 # Cosinüs teoremi
            cv2.putText(frame,str(int(angle)),(enSag[0]-10,enSag[1]-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        except:
            cv2.putText(frame,"?",(enSag[0]-10,enSag[1]-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)

    if cv2.waitKey(1) & 0xFF == 27: # ESC tuşuna basıldığında
        break

cap.release()
cv2.destroyAllWindows() # Pencereleri kapat
