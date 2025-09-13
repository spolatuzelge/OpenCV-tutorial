
#-----------------#
#   EŞİKLEME  
#-----------------#


import cv2

img = cv2.imread(r"materyal\cokgen.png")

esik=127

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

for i in range(5):
    ret ,binary =cv2.threshold(gray,esik,255,i)
    cv2.imshow("binary_"+str(i),binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
