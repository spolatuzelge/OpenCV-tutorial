
#----------------------------------------------------#
# Tuval Oluşturma  ve Resim Üzerinde Çizim İşlemleri
#----------------------------------------------------#

import cv2
import numpy as np

img=cv2.imread(r"materyal\logo.png") # Resmi oku
cv2.namedWindow("Logo",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Logo",img)
cv2.waitKey(0)

m1 = np.copy(img) # img.copy() şeklinde de yapılabilir. img değişkeninin kopyasını alır.
m2 = img

img[100:200,200:300,:] =0 # 100-200 ve 200-300 aralığındaki pikselleri siyah yapar.
cv2.imshow("m2",m2) # m2 değişkeni img değişkenine referans olduğu için img değişkeninde yapılan değişiklikler m2 değişkenine de yansır.
cv2.waitKey(0)

m3 =np.zeros(img.shape, img.dtype) # img değişkeninin boyutlarında ve veri tipinde bir matris oluşturur.
cv2.imshow("m3",m3)
cv2.waitKey(0)


m4 = np.zeros((512,512),np.uint8) # (512 x 512) boyutlarında ve 8 bitlik bir matris oluşturur. Tuval oluşturur.
cv2.imshow("m4",m4)
cv2.waitKey(0)

m5 = np.zeros((512,512),np.uint8) # (512 x 512) boyutlarında ve 8 bitlik bir matris oluşturur. Tuval oluşturur.
m5[:,:] = 127 # Tüm pikselleri gri yapar. 127 gri tonu
cv2.imshow("m5",m5)
cv2.waitKey(0)


# Resim cizme

m6 = np.ones((550,770,3))
black = (0,0,0)
red = (0,0,255)
green = (0,255,0)

cv2.rectangle(m6,(480,250),(100,450),black,8)
cv2.rectangle(m6,(580,150),(200,350),black,8)
cv2.line(m6,(480,250),(580,150),black,8)
cv2.line(m6,(100,450),(200,350),black,8)
cv2.line(m6,(480,450),(580,350),black,8)
cv2.line(m6,(100,250),(200,150),black,8)

startPoint = (150,100)
font_thickness = 5
font_size = 2
font=cv2.FONT_HERSHEY_DUPLEX

cv2.putText(m6,"OpenCV",startPoint,font,font_size,black,font_thickness)
cv2.imshow("m6",m6)
cv2.waitKey(0)