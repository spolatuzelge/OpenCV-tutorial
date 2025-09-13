

#----------------------------------------#
# HOG(Histogram of Oriented Gradients) 
#-----------------------------------------#

import cv2
import numpy as np

img = cv2.imread(r"materyal\person.png") # Resmi okuma işlemi
hog = cv2.HOGDescriptor() # HOG nesnesi oluşturma işlemi
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) # HOG nesnesine insan tespiti için kullanılacak modeli atama işlemi
boxes, weights = hog.detectMultiScale(img, winStride=(8, 8), padding=(32, 32), scale=1.05) # HOG nesnesi ile insan tespiti işlemi

for i, (x, y, w, h) in enumerate(boxes):
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) # Dikdörtgen çizme işlemi
    cv2.putText(img, f"Person {i + 1}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) # Metin ekleme işlemi

cv2.imshow("HOG", img) # Resmi ekranda gösterme işlemi
cv2.waitKey(0) # Bekleme işlemi
cv2.destroyAllWindows() # Pencereleri kapatma işlemi
