

" ---------------------------------------------- "
# Hough Circle Transform (Hough Daire Dönüşümü) 
" ---------------------------------------------- "

import cv2
import numpy as np

ballons = cv2.imread("materyal\\klasor10\\baloon.jpg")
para = cv2.imread("materyal\\klasor10\\para.jpg")

greyBallons = cv2.cvtColor(ballons, cv2.COLOR_BGR2GRAY)
greyPara = cv2.cvtColor(para, cv2.COLOR_BGR2GRAY)

blurBallons = cv2.medianBlur(greyBallons, 5)
blurPara = cv2.medianBlur(greyPara, 5)

circleBallons = cv2.HoughCircles(blurBallons, cv2.HOUGH_GRADIENT, 1, ballons.shape[0]/4, param1=200, param2=10, minRadius=5, maxRadius=30)
circlePara = cv2.HoughCircles(blurPara, cv2.HOUGH_GRADIENT, 1, para.shape[0]/4, param1=200, param2=10, minRadius=15, maxRadius=89)
# cv2.HoughCircles(image, method, dp, minDist, param1, param2, minRadius, maxRadius)
# method: kullanılacak algortima
# dp: çözünürlük oranı
# minDist: algortima için gerekli olan minimum mesafe
# param1: canny edge detector için birinci eşik değeri
# param2: canny edge detector için ikinci eşik değeri
# minRadius: dairenin minimum yarıçapı
# maxRadius: dairenin maksimum yarıçapı

if circleBallons is not None:
    circleBallons = np.uint16(np.around(circleBallons))
    for i in circleBallons[0, :]:
        cv2.circle(ballons, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(ballons, (i[0], i[1]), 2, (0, 0, 255), 3)

if circlePara is not None:
    circlePara = np.uint16(np.around(circlePara))
    for i in circlePara[0, :]:
        cv2.circle(para, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(para, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow("Ballons", ballons)
cv2.imshow("Para", para)

cv2.waitKey(0)
cv2.destroyAllWindows()