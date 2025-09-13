

" ----------------------------------------------------- "
# Videoleın Renk Uzayı Dönüşümleri
" ----------------------------------------------------- "


import cv2
import numpy as np

cap = cv2.VideoCapture("materyal\\klasor8\\klasor8_video.mp4")

while True:
    ret,frame = cap.read()
    if not ret:
        break

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR -> RGB
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # BGR -> HSV
    frameGRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # BGR -> GRAY

    cv2.imshow("Orjinal", frame)
    cv2.imshow("RGB", frameRGB)
    cv2.imshow("HSV", frameHSV)
    cv2.imshow("GRAY", frameGRAY)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()