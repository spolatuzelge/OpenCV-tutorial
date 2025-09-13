

" --------------------------------- "
# TrackBar Uygulaması
" --------------------------------- "

import cv2
import numpy as np

def nothing(x):
    pass

tuval = np.zeros((512, 512, 3), dtype="uint8") + 255
cv2.namedWindow("Tuval")

cv2.createTrackbar("Red"  , "Tuval", 0, 255, nothing)
cv2.createTrackbar("Green", "Tuval", 0, 255, nothing)
cv2.createTrackbar("Blue" , "Tuval", 0, 255, nothing)
cv2.createTrackbar("Switch", "Tuval", 0, 1, nothing)

while True:
    cv2.imshow("Tuval", tuval)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    r = cv2.getTrackbarPos("Red", "Tuval")
    g = cv2.getTrackbarPos("Green", "Tuval")
    b = cv2.getTrackbarPos("Blue", "Tuval")
    s = cv2.getTrackbarPos("Switch", "Tuval")
    
    if s == 0:
        tuval[:] = 255
    else:
        tuval[:] = [b, g, r]

cv2.destroyAllWindows()

