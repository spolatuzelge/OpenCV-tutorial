

#--------------------------------------------------------------#
# GÖRÜNTÜ İŞLEMEDE İSTATİSTİKSEL İŞLEMLER VE TRESHOLD İŞLEMİ
#--------------------------------------------------------------#


import cv2
import numpy as np


img = cv2.imread(r"materyal\logo.png",cv2.IMREAD_GRAYSCALE)

#min ve max degeri bulma
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img) # min ve max degerleri ve koordinatlarini bulur
print("min degeri: ",min_val)
print("max degeri: ",max_val)
print("min degerinin koordinatlari: ",min_loc)
print("max degerinin koordinatlari: ",max_loc)


#ortalama ve standart sapma degeri bulma
mean, std = cv2.meanStdDev(img) # ortalama ve standart sapma degerlerini hesaplar
print("ortalama: ",mean)
print("standart sapma: ",std)



# ORTALAMA DEĞER İLE TRESHOLD İŞLEMİ

img[img < mean] = 0 # ortalama degerinden küçük olan pikselleri siyah yap
img[img > mean] = 255 # ortalama degerinden büyük olan pikselleri beyaz yap

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()