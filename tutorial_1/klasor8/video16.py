

" -------------------------------------------------------------------- "
# Görüülerdeki Kenarları Bulma
# Canny Edge Detection--> cv2.Canny() :input, minTreshol, maxTreshold
" -------------------------------------------------------------------- "

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 255)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Edges", edges)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()