
#----------------------------------------------------#
# KAMERA GİRİŞİNİ OKUMA VE İŞLEME İŞLEMLERİ
#----------------------------------------------------#

import cv2

cap = cv2.VideoCapture(0)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
print("height:",height,"width:",width,"count:",count,"fps:",fps)


def process (image, opt =1): # opt = 0: tersleme, opt = 1: bulanıklaştırma, opt = 2: kenar bulma
    dst = None
    if opt == 0:
        dst = cv2.bitwise_not(image) # Tersleme işlemi
    if opt == 1:
        dst = cv2.GaussianBlur(image,(0,0),15) # 15: standart sapma değeri
    if opt == 2:
        dst=cv2.Canny(image,100,200) # 100 ve 200 değerleri eşik değerleridir.
    return dst

index = 1 # Varsayılan işlem: bulanıklaştırma
while True: # Sonsuz döngü
    ret,frame = cap.read() # Kameradan bir kare oku
    frame=cv2.flip(frame,1) # Yatay olarak çevir
    if ret == True:
        cv2.imshow("video-input",frame) # Kameradan alınan kareyi göster 
        c= cv2.waitKey(50) # 50 ms bekle
        if c >= 49: # 1-9 arası tuşlara basıldığında
            index = c-49 # index değerini güncelle
        result = process(frame,index) # İşlemi uygula
        cv2.imshow("result",result) # İşlem sonucunu göster
        if c ==27: # ESC tuşuna basıldığında
            break # Döngüyü sonlandır 
    else:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
