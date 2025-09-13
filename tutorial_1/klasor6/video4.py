

" --------------------------------- "
# Resim Okuma, Gösterme ve Kaydetme
#[cv2.imread(), cv2.imwrite(), cv2.imshow(), cv2.waitKey(), cv2.destroyAllWindows(), cv2.namedWindow()]
" --------------------------------- "

import cv2

img = cv2.imread("materyal\\klasor6\\klon.jpg") # Okunacak Resmin Dosya Yolu 

imgGri= cv2.imread("materyal\\klasor6\\klon.jpg", 0) # Okunacak Resmin Dosya Yolu ve Resmin Gri Tonlama İle Okunması
cv2.imwrite("materyal\\klasor6\\klonGriVideo4.jpg", imgGri)

### Resimlerin Matematiksel Değerleri  İçin ###
# print(img)
#############################################

cv2.namedWindow("Klon", cv2.WINDOW_NORMAL) # Pencere Oluşturma, İlk Parametre Pencerenin Adı, İkinci Parametre Pencere Boyutu
cv2.imwrite("materyal\\klasor6\\klonVideo4.jpg", img) # Resmi Kaydetme, İlk Parametre Kaydedilecek Resmin Adı, İkinci Parametre Resmin İçeriği
cv2.imshow("Klon", img) # Resmi Gösterme , İlk Parametre Pencerenin Adı, İkinci Parametre Resmin İçeriği
cv2.waitKey(0) # Pencereyi Kapatmak İçin Bir Tuşa Basılmasını Bekler
cv2.destroyAllWindows() # Tüm Pencereleri Kapatır