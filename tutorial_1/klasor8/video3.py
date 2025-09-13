

" --------------------------------- "
# Görüntülerde Toplama İşlemi
#[cv.add(), ]
" --------------------------------- "

import cv2
import numpy as np

circle = np.zeros((512,512, 3), dtype="uint8") + 255
cv2.circle(circle, (256,256), 60, (255,0,0), -1)

rectangle = np.zeros((512,512, 3), dtype="uint8") + 255
cv2.rectangle(rectangle, (150,150), (350,350), (0,0,225), -1)

add = cv2.add(circle, rectangle) # İki görüntüyü toplar
print(add[256,256])

cv2.imshow("Add", add)
cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)


cv2.waitKey(0)
cv2.destroyAllWindows()