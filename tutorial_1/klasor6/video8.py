

" --------------------------------- "
# Video Okuma ve Gösterme
# [.VideoCapture() , cv.flip() , cv.release()]
" --------------------------------- "

import cv2

#### Kameradan Görüntü Almak ####
cap = cv2.VideoCapture(0) # 0 = İlk Kamera, 1 = İkinci Kamera

#### MP4 Video Dosyasından Görüntü Almak ####
#cap = cv2.VideoCapture("materyal\\klasor6\\klasor6_video.mp4")


while True: # Sonsuz Döngü, Kamera Açık Olduğu Sürece Çalışır
    ret, frame = cap.read() # Kameradan Gelen Görüntüyü Okur
    
    if ret == False: # Eğer Görüntü Alınamazsa
        break

    frame = cv2.flip(frame, 1) # Görüntüyü Yatay Olarak Çevirir

    cv2.imshow("Video_8", frame) # Görüntüyü Gösterir

    if cv2.waitKey(1) & 0xFF == ord("q"): # Eğer Q Tuşuna Basılırsa
        break # Döngüyü Sonlandır

cap.release() # Kamerayı Kapat, Belleği Boşalt, İşlemciyi Serbest Bırak
cv2.destroyAllWindows()