# ornek : 0-40-70 62-207-255

" ---------------------------------------- "
# Aıştırma - Renklerin HSV Kodlarını Bulma
" ---------------------------------------- "


import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 500, 250)

cv2.createTrackbar("Lower H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("Lower S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Lower V", "Trackbars", 0, 255, nothing)

cv2.createTrackbar("Upper H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("Upper S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Upper V", "Trackbars", 0, 255, nothing)

# HSV renk aralığı için üst sınırların en yüksek değerlerinden başlatıyoruz
cv2.setTrackbarPos("Upper H", "Trackbars", 180)
cv2.setTrackbarPos("Upper S", "Trackbars", 255)
cv2.setTrackbarPos("Upper V", "Trackbars", 255)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower H", "Trackbars")
    lower_s = cv2.getTrackbarPos("Lower S", "Trackbars")
    lower_v = cv2.getTrackbarPos("Lower V", "Trackbars")

    upper_h = cv2.getTrackbarPos("Upper H", "Trackbars")
    upper_s = cv2.getTrackbarPos("Upper S", "Trackbars")
    upper_v = cv2.getTrackbarPos("Upper V", "Trackbars")

    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv, lower_color, upper_color)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()