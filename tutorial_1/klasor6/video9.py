

" --------------------------------- "
# Video Kaydetme
" --------------------------------- "

import cv2

cap = cv2.VideoCapture(0)

videoFileOutput = cv2.VideoWriter("materyal\\klasor6\\klasor6_video9.mp4", 
                                  cv2.VideoWriter_fourcc(*"mp4v"), 
                                  20, 
                                  (640, 480))
# Video Adı, Video Formatı, FPS, Çözünürlük

while True:
    ret, frame = cap.read()
    
    if ret == False:
        break

    frame = cv2.flip(frame, 1)
    videoFileOutput.write(frame)

    cv2.imshow("Video_9", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()