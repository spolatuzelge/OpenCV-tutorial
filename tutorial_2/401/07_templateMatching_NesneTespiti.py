

#-------------------------------------#
# TEMPLATE MATCHING (NESNE TESPİTİ)
#-------------------------------------#

import cv2
import numpy as np


def TemplateMatching(img, template):
    
    template_H = template.shape[0] # Template yükseklik değeri
    template_W = template.shape[1] # Template genişlik değeri

    detec = cv2.matchTemplate(img, template, method=cv2.TM_CCORR_NORMED) # Template Matching işlemi
    # matchTemplate(resim, template, method), method: Template Matching yöntemi, TM_CCOEFF_NORMED: Korelasyon katsayısı
    #cv2.imshow("Detected", detec) # Resmi ekranda gösterme işlemi

    t = 0.95 # Eşik değeri
    loc = np.where(detec > t) # Template Matching sonucunda eşik değeri üzerindeki değerleri bulma işlemi

    for i in zip(*loc[::-1]):
        cv2.rectangle(img, i, (i[0] + template_W, i[1] + template_H), (255, 255, 0), 1,8,0) # Dikdörtgen çizme işlemi
        cv2.putText(img, "Detected", (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)# Metin ekleme işlemi
    
    cv2.imshow("Template Matching", img) # Resmi ekranda gösterme işlemi

img = cv2.imread(r"materyal\openCV.png") # Resmi okuma işlemi
template = cv2.imread(r"materyal\sablon.png") # Template resmi okuma işlemi

TemplateMatching(img, template) # Template Matching fonksiyonunu çağırma işlemi

cv2.waitKey(0) # Bekleme işlemi
cv2.destroyAllWindows() # Pencereleri kapatma işlemi
