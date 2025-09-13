

#----------------------#
# HİSTOGRAM EŞİTLEME
#----------------------#

# Histogram eşitleme, bir resmin kontrastını arttırmak için kullanılan bir tekniktir.

import cv2
import numpy as np
from matplotlib import pyplot as plt

def costum_hist(x):
    h, w = x.shape[:2] # yükseklik ve genişlik değerlerini alır.
    hist = np.zeros([256], dtype=np.int32) # 256 adet 0 değerinden oluşan bir dizi oluşturur.
    for row in range(h):
        for col in range(w):
            pv = x[row, col]
            hist[x[row, col]] += 1
    
    yPos = np.arange(0, 256,1, dtype=np.int32)
    plt.bar(yPos, hist, align='center', alpha=0.5, color='b')
    plt.xticks(yPos,yPos)
    plt.ylabel('Frekans')
    plt.title('Histogram')
    plt.show()

img = cv2.imread(r"materyal\yesillik.jpg") # Gri tonlamalı olarak resmi okur.
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Resmi gri tonlamalıya çevirir.
costum_hist(img) # Gri tonlamalı görsel için histogram oluşturur.
dst = cv2.equalizeHist(img) # Histogram eşitleme işlemi yapılır.
costum_hist(dst) # Histogram eşitlenmiş görsel için histogram oluşturur.
cv2.imshow("Histogram Esitleme", dst)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()