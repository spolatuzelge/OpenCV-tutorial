

#------------------------------#
# RENK UZAYININ DEĞİŞTİRİLMESİ
#------------------------------#

import cv2

# HSV  : Hue, Saturation, Value : Renk, Doyma, Parlaklık, Bu renk uzayı nesnelerin takibini kolaylaştırır.

img = cv2.imread(r"materyal\openCV.png")
cv2.namedWindow("BGR", cv2.WINDOW_AUTOSIZE)
cv2.imshow("BGR", img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR'den GRAY'e dönüşüm
cv2.namedWindow("GRAY", cv2.WINDOW_AUTOSIZE)
cv2.imshow("GRAY", imgGray)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # BGR'den HSV'ye dönüşüm
cv2.namedWindow("HSV", cv2.WINDOW_AUTOSIZE)
cv2.imshow("HSV", imgHSV)


cv2.waitKey(0)
cv2.destroyAllWindows()