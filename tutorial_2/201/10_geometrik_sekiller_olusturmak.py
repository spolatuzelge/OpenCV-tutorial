

#---------------------------------------------------------#
#  GEOMETRİK ŞEKİLLER OLUŞTURMAK VE ANİMASYON OLUŞTURMAK
#---------------------------------------------------------#

import  cv2 
import numpy as np

img = np.zeros((512,512,3),dtype="uint8") # (512X512) boyutlarında siyah bir resim oluştur

cv2.rectangle(img,(100,100),(300,300),(255,0,0),2,cv2.LINE_8,0) # 2: kalınlık, cv2.LINE_8: çizgi tipi
cv2.circle(img,(256,256),50,(0,0,255),2,cv2.LINE_8,0) # 50: yarıçap 
cv2.ellipse(img,(256,256),(150,50),360,0,360,(0,255,0),2,cv2.LINE_8,0) # 150: büyük eksen, 50: küçük eksen
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


for i in range(100000): 
    img [:,:,:]=0
    x1 = np.random.rand()*512 # 0-1 arası rastgele bir sayı üret 
    y1 = np.random.rand()*512 # 0-1 arası rastgele bir sayı üret 
    x2 = np.random.rand()*512 # 0-1 arası rastgele bir sayı üret 
    y2 = np.random.rand()*512 # 0-1 arası rastgele bir sayı üret 

    b=np.random.randint(0,256) # 0-255 arası rastgele bir sayı üret
    g=np.random.randint(0,256) # 0-255 arası rastgele bir sayı üret
    r=np.random.randint(0,256) # 0-255 arası rastgele bir sayı üret 

    cv2.line(img,(int(x1),int(y1)),(int(x2),int(y2)),(b,g,r),2,cv2.LINE_8,0) # 2: kalınlık, cv2.LINE_8: çizgi tipi 
    cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(b,g,r),2,cv2.LINE_8,0) # 2: kalınlık, cv2.LINE_8: çizgi tipi 
    cv2.imshow("img",img)
    c=cv2.waitKey(20)
    if c==27:
        break

cv2.destroyAllWindows()
