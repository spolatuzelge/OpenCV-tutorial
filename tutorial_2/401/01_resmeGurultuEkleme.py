

#----------------------------------------------------#
# RESME GÜRÜLTÜ EKLEME İŞLEMİ (IMAGE NOISE ADDITION)
#----------------------------------------------------#

import cv2
import numpy as np

def addSaltPepper(x): # Tuz-Biber Gürültüsü Ekleme Fonksiyonu (Salt-Pepper Noise)
    h, w = x.shape[:2] # Resmin yükseklik ve genişlik değerlerini alır. 
    nums = 1000 # Gürültü eklenecek piksel sayısı 

    rows = np.random.randint(0, h, nums, dtype= np.int32) # 0 ile h arasında rastgele sayılar üretir.
    cols = np.random.randint(0, w, nums, dtype= np.int32) # 0 ile w arasında rastgele sayılar üretir.

    for i in range(nums): # Gürültü ekleme işlemi
        if i % 2 == 0: # Tuz-Biber gürültüsü ekleme işlemi
            x[rows[i], cols[i]] = 0 # Siyah renk (0) ekleme işlemi 
        else:
            x[rows[i], cols[i]] = 255 # Beyaz renk (255) ekleme işlemi
    return x

img = cv2.imread(r"materyal\openCV.png" )

h, w = img.shape[:2] # Resmin yükseklik ve genişlik değerlerini alır.
copy = np.copy(img) # Resmin kopyasını alır.

copy = addSaltPepper(copy) # Tuz-Biber gürültüsü ekleme işlemi

result = np.concatenate((img, copy), axis=1) # Resimleri birleştirme işlemi

cv2.imshow("Salt-Pepper Noise", result) # Resmi ekranda gösterme işlemi
cv2.waitKey(0) # Bekleme işlemi
cv2.destroyAllWindows() # Pencereleri kapatma işlemi
