

#----------------------#
# HİSTOGRAM OLUŞTURMAK
#----------------------#

# Histogram, bir resimdeki piksel değerlerinin dağılımını gösteren bir grafiktir.

import cv2
import numpy as np
from matplotlib import pyplot as plt


# Aşağıdaki fonksiyon, gri tonlamalı görseller için histogram oluşturur.
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

# Aşağıdaki fonksiyon, renkli görseller için histogram oluşturur.
def costum_hist2(x):
    cv2.imshow("Original", x)
    color = ('b', 'g', 'r')
    for i, c in enumerate(color):
        hist = cv2.calcHist([x], [i], None, [256], [0, 256])
        plt.plot(hist, color=c)
        plt.xlim([0, 256])
    plt.title('Histogram')
    plt.show()


img = cv2.imread(r"materyal\yesillik.jpg") # Gri tonlamalı olarak resmi okur.

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Resmi gri tonlamalı hale getirir.
costum_hist(imgGray) # Gri tonlamalı görsel için histogram oluşturur.
costum_hist2(img) # Renkli görsel için histogram oluşturur.

cv2.namedWindow("Original", cv2.WINDOW_AUTOSIZE) 
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
