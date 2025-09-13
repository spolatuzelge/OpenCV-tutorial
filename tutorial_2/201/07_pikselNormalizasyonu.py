#-------------------------#
# PİKSEL NORMALİZASYONU
#------------------------#


import cv2
import numpy as np
 

# Aynı şeyleri farklı sayılarla temsil ettirmiş oluyoruz.
 
img = cv2.imread(r"C:\Users\polat\Desktop\turkceGelecegiYazanlar\TGY\OpenCV\OpenCV201\materyal\cokgen.png")
print(img.shape) # (height, width, channel) -> (512, 512, 3)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray",gray)
#cv2.waitKey(0)

print(gray.shape) # (height, width) -> (512, 512)
print(gray)

"""gray = np.float32(gray) # float32 tipine dönüştürdük
print(gray)"""

"""dst = np.zeros(gray.shape,dtype="float32") # 0'lardan oluşan bir matris oluşturduk

cv2.normalize(gray,dst=dst,alpha=0,beta=1.0,norm_type=cv2.NORM_MINMAX) # 0-1 arasına normalize ettik, en küçük değeri 0 yaptık
print(dst)

print(np.uint8(dst*255))

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(dst) # min ve max değerleri ve koordinatlarını bulduk
print("min degeri: ",min_val)
print("max degeri: ",max_val)
print("min degerinin koordinatlari: ",min_loc)
print("max degerinin koordinatlari: ",max_loc)

mean, std = cv2.meanStdDev(np.uint8(dst*255))
print("ortalama: ",mean)
print("standart sapma: ",std)"""


### NORM_INF 
dst = np.zeros(gray.shape,dtype="float32")
cv2.normalize(gray,dst=dst,alpha=0,beta=1.0,norm_type=cv2.NORM_INF) # 0-1 arasına normalize ettik, en büyük değeri 1 yaptık 
print(dst)
cv2.imshow("dst",np.uint8(dst*225))
cv2.waitKey(0)


### NORM_L1
dst = np.zeros(gray.shape,dtype="float32")
cv2.normalize(gray,dst=dst,alpha=0,beta=1.0,norm_type=cv2.NORM_L1) # 0-1 arasına normalize ettik, toplam değer 1 olacak şekilde
print(dst)
cv2.imshow("dst",np.uint8(dst*225))
cv2.waitKey(0)

