

" --------------------------------- "
# Video Okuma ve Gösterme - Telefon Kamerası
" --------------------------------- "

import cv2
import numpy
import requests

url  = "http://192.168.137.54:8080//shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = numpy.array(bytearray(img_resp.content), dtype=numpy.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (640, 480))

    cv2.imshow("Android Camera", img)

    if cv2.waitKey(1) == 27: # 27 = ESC
        break

cv2.destroyAllWindows()