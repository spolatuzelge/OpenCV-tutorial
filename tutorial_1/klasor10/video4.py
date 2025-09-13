

" ---------------------------------------------------- "
# Hough Line Transform (Hough Doğru Dönüşümü) - Video 
" ---------------------------------------------------- "

import cv2
import numpy as np

video = cv2.VideoCapture("materyal\\klasor10\\line.mp4")

while True:
    ret, frame = video.read()
    if not ret: # video bittiğinde döngüyü kır , hata almayı engeller
        break

    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # hsv formatına çevirme

    lower_yellow = np.array([18, 94, 140],np.uint8) # sarı rengin alt sınırı
    upper_yellow = np.array([48, 255, 255],np.uint8) # sarı rengin üst sınırı

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow) # sarı rengi maskeleme

    edges = cv2.Canny(mask, 75, 250) # kenarları bulma


    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50,maxLineGap =50) 
    # cv2.HoughLines(image, rho, theta, threshold, lines)
    # rho: polar koordinatlarının birimleri
    # theta: radyan cinsinden açılar
    # threshold: eşik değeri
    # lines: çıktı doğruları

    print(lines)

    for line in lines:
        (x1, y1, x2, y2) = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        
    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()
video.release()


