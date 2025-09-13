
#-----------------------------------------------#
# VİDEO ALMAK , GÖSTERME VE KAYDETME İŞLEMLERİ
#-----------------------------------------------#

import cv2
import numpy as np

cap = cv2.VideoCapture(r"materyal\yol.mp4") # Video dosyasını oku

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Video dosyasının yüksekliğini al
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Video dosyasının genişliğini al
count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # Video dosyasındaki toplam frame sayısını al
fps = cap.get(cv2.CAP_PROP_FPS) # Video dosyasının fps değerini al

print("height: ",height) 
print("width: ",width)
print("count: ",count)
print("fps: ",fps)


out = cv2.VideoWriter("materyal\yol_norm_inf.avi",cv2.VideoWriter_fourcc("D","I","V","X"),15,(width,height),True) # Video dosyasını kaydet


# Video dosyasını oku ve kaydet
while True:
    ret,frame = cap.read()

    if ret == True:
        cv2.imshow("frame",frame)
        out.write(frame) # Video dosyasını kaydet (yazdır)
        c= cv2.waitKey(50)
        if c == 27:
            break
    else:
        break    
cap.release() # Video dosyasını serbest bırak
out.release() # Video dosyasını kaydet
cv2.destroyAllWindows()
