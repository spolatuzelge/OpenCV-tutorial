

" --------------------------------------- "
# Görüntülerde Ağırlıklı Toplama İşlemi
# [cv.addWeighted(), ]
" -------------------------------------- "


import cv2
import numpy as np

circle = np.zeros((512,512, 3), dtype="uint8") + 255
cv2.circle(circle, (256,256), 60, (255,0,0), -1)

rectangle = np.zeros((512,512, 3), dtype="uint8") + 255
cv2.rectangle(rectangle, (150,150), (350,350), (0,0,225), -1)

dst = cv2.addWeighted(circle, 0.7, rectangle, 0.3, 0) # İki görüntüyü ağırlıklı toplar, 0.7 ve 0.3 oranlarında

cv2.imshow("Add", dst)
cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)

cv2.waitKey(0)
cv2.destroyAllWindows()