

" ----------------------------------------------- "
# Morfolojik İşlemler - Erosion
# Karakter (yazı) tanıma işlemlerinde kullanılır.
" ----------------------------------------------- "


import cv2
import numpy as np

img = cv2.imread("materyal\\klasor8\\helikopter2.png",0)

kernel1 = np.ones((5,5),np.uint8) # 5x5 lik bir kernel oluşturulur.
kernel2 = np.ones((3,3),np.uint8) # 3x3 lük bir kernel oluşturulur.
kernel3 = np.ones((7,7),np.uint8) # 7x7 lik bir kernel oluşturulur.


############### Erosion İşlemi ###############
erosion1 = cv2.erode(img,kernel1,iterations = 2) #erosion işlemi yapılır
erosion2 = cv2.erode(img,kernel2,iterations = 2) #erosion işlemi yapılır
erosion3 = cv2.erode(img,kernel3,iterations = 2) #erosion işlemi yapılır

cv2.imshow("Orjinal Resim",img)
cv2.imshow("Erosion Resim",erosion1)
cv2.imshow("Erosion Resim2",erosion2)
cv2.imshow("Erosion Resim3",erosion3)
####################################################################################

############### Dilatation İşlemi - Kalınlaştırma ###############
dilatation1 = cv2.dilate(img,kernel1,iterations = 2) 
dilatation2 = cv2.dilate(img,kernel2,iterations = 2) 
dilatation3 = cv2.dilate(img,kernel3,iterations = 2) 

cv2.imshow("Dilatation Resim",dilatation1)
cv2.imshow("Dilatation Resim2",dilatation2)
cv2.imshow("Dilatation Resim3",dilatation3)
####################################################################################

############### Opening İşlemi - Erosion + Dilatation ###############
opening1 = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel1)
opening2 = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel2)
opening3 = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel3)

cv2.imshow("Opening Resim",opening1)
cv2.imshow("Opening Resim2",opening2)
cv2.imshow("Opening Resim3",opening3)
####################################################################################

############### Closing İşlemi - Dilatation + Erosion ###############
closing1 = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel1)
closing2 = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel2)
closing3 = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel3)

cv2.imshow("Closing Resim",closing1)
cv2.imshow("Closing Resim2",closing2)
cv2.imshow("Closing Resim3",closing3)
####################################################################################

############### Gradient İşlemi - Dilatation - Erosion ###############
gradient1 = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel1)
gradient2 = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel2)
gradient3 = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel3)

cv2.imshow("Gradient Resim",gradient1)
cv2.imshow("Gradient Resim2",gradient2)
cv2.imshow("Gradient Resim3",gradient3)
####################################################################################

############### Top Hat İşlemi - Orjinal - Opening ###############
tophat1 = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel1)
tophat2 = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel2)
tophat3 = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel3)

cv2.imshow("Top Hat Resim",tophat1)
cv2.imshow("Top Hat Resim2",tophat2)
cv2.imshow("Top Hat Resim3",tophat3)
####################################################################################

############### Black Hat İşlemi - Closing - Orjinal ###############
blackhat1 = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel1)
blackhat2 = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel2)
blackhat3 = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel3)

cv2.imshow("Black Hat Resim",blackhat1)
cv2.imshow("Black Hat Resim2",blackhat2)
cv2.imshow("Black Hat Resim3",blackhat3)
####################################################################################

cv2.waitKey(0)
cv2.destroyAllWindows()