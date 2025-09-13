

#------------------------------#
# İKİ RESMİ BİRLEŞTİRME İŞLEMİ 
#------------------------------#

import cv2
import numpy as np

img1=cv2.imread(r"materyal\logo.png")
img2=cv2.imread(r"materyal\logo_gray.png")

birlesik = np.hstack((img1,img2)) # Resimleri yatay olarak birleştirir.


cv2.imshow("Birlesik",birlesik) # Resmi göster
cv2.namedWindow("Birlesik",cv2.WINDOW_NORMAL) # Pencere oluştur
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekle
cv2.destroyAllWindows()

