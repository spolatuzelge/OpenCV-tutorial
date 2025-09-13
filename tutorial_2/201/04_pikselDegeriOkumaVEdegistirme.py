

#----------------------------------------------------#
# Piksel değerlerini okuma ve yazma işlemleri
#----------------------------------------------------#

import cv2

img = cv2.imread(r"materyal\logo.png") # Resmi oku
cv2.namedWindow("Logo",cv2.WINDOW_AUTOSIZE) # Pencere oluştur 


h,w,ch = img.shape # .shape fonksiyonu ile resmin yüksekliği, genişliği ve kanal sayısı alınır.
print("h:",h,"w:",w,"ch:",ch)

for row in range(h): # Resmin tüm pikselleri üzerinde dolaşma
    for col in range(w): # Resmin tüm pikselleri üzerinde dolaşma
        b,g,r = img[row,col] # Piksel değerlerini al 
        b=255-b # Mavi kanalı tersine çevir
        g=255-g # Yeşil kanalı tersine çevir
        r=255-r # Kırmızı kanalı tersine çevir
        img[row,col] = (b,g,0) # Piksel değerlerini değiştir

cv2.imshow("Logo",img) # Resmi göster
cv2.waitKey(0)
cv2.destroyAllWindows()