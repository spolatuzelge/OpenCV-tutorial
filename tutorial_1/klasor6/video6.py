

" --------------------------------- "
# En Boy Oranı (Aspect Ratio) Uygulaması
# [.shape() , ]
" --------------------------------- "

import cv2

def resizeWith_AspectRatio(img,widht= None, height= None, inter = cv2.INTER_AREA):
    dimesion = None # Boyutları Belirlemek İçin None Değer Atanır
    (h, w) = img.shape[:2] # Resmin Yükseklik ve Genişliği Alınır. img.shape[0] = Yükseklik, img.shape[1] = Genişlik

    if widht is None and height is None: # Eğer Genişlik ve Yükseklik Belirtilmemişse, Resim Orjinal Boyutunda Kalır
        return img
    
    if widht is None: # Eğer Genişlik Belirtilmemişse
        r = height / float(h) # Oran Hesaplanır
        dimesion = (int(w * r), height)

    else: # Eğer Genişlik Belirtilmişse
        r = widht / float(w)
        dimesion = (widht, int(h * r))

    return cv2.resize(img, dimesion, interpolation = inter)

img = cv2.imread("materyal\\klasor6\\\\klon.jpg")
img1 = resizeWith_AspectRatio(img, height=600)
cv2.imshow("Original", img)
cv2.imshow("Resized", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()