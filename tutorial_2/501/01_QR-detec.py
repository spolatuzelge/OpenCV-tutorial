

#--------------------
# QR CODE DETECTION
#--------------------

import cv2
import numpy as np

img = cv2.imread(r'materyal\qr.png')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detector = cv2.QRCodeDetector() # Bu fonksiyon QR kodu algılamak için kullanılır. Çıkış olarak QR kodunun verilerini ve konumunu döndürür.

data, bbox, straight_qrcode = detector.detectAndDecode(img)

result = np.copy(img)

cv2.drawContours(result, [np.int0(bbox)], 0, (0, 0, 255), 2)

cv2.imshow('Result', result)
print("Decoded Data : {}".format(data))
cv2.waitKey(0)
cv2.destroyAllWindows()