

" -------------------------------------- "
# Çözünürlük Ayarlama (Set Resolution)
" -------------------------------------- "

import cv2

pencereAdi = "Kamera"
cv2.namedWindow(pencereAdi)

cap = cv2.VideoCapture(0) # Webcam'den görüntü almak için 0,1,2... gibi değerler kullanılır.
print("Widht: ", cap.get(3)) # Genişlik
print("Height: ", cap.get(4)) # Yükseklik

cap.set(3, 1280) # Yeni Genişlik
cap.set(4, 720) # Yeni Yükseklik

print("Widht*: ", cap.get(3)) # Genişlik
print("Height*: ", cap.get(4)) # Yükseklik

while True:
    _ , frame = cap.read() # Görüntüyü okuma
    frame = cv2.flip(frame, 1) # Görüntüyü yatayda çevirme

    cv2.imshow(pencereAdi, frame)

    if cv2.waitKey(1) == 27: # 27 tuşu ESC tuşudur.
        break

cap.release()
cv2.destroyAllWindows()