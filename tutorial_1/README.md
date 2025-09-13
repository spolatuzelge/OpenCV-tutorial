# 🎓 Udemy OpenCV Eğitim Notları

Bu repoda, **Udemy OpenCV eğitimi** temel alınarak hazırlanmış Python örnekleri yer almaktadır. Her klasör, belirli bir konu başlığını ele almakta ve ilgili işlemler Jupyter Notebook veya Python script dosyaları üzerinden gösterilmektedir.

> 🧠 Tüm içerik, öğrenme amacıyla yeniden yapılandırılmıştır. Kodlar, eğitim videolarıyla senkronize olacak şekilde düzenlenmiş; ek açıklamalar ve geliştirmeler yapılmıştır.

---

## 📂 Klasörler ve İçerikler

### `klasor6/` – Temel Video ve Görüntü İşlemleri
- Görüntü okuma, gösterme, kaydetme
- Video yakalama (`cv2.VideoCapture`)
- Görüntü yeniden boyutlandırma ve video kaydetme

### `klasor7/` – Çekirdek ve Grafik Fonksiyonları
- Temel görüntü matematiği işlemleri
- `draw` ve `trackbar` kullanımı
- Görüntü üzerine yazı yazma

### `klasor8/` – Renk Uzayı, Maskeleme ve Filtreleme
- HSV renk uzayıyla renk ayrımı
- ROI, piksel işleme, histogram
- Bitwise işlemler
- `warpAffine`, kenar tespiti (`Canny`, `Sobel`)
- Erozyon, eşikleme, köşe tespiti

### `klasor9/` – Kontur Algılama ve Şekil Özellikleri
- Kontur çıkarımı (`cv2.findContours`)
- Moment hesaplama, kontur alanı
- Convex Hull ve konveks kusur analizi

### `klasor10/` – Hough Dönüşümleri
- Doğru tespiti: `cv2.HoughLines`, `cv2.HoughLinesP`
- Daire tespiti: `cv2.HoughCircles`
- Gerçek zamanlı video üzerinde uygulama

### `klasor11/` – Şekil Tanıma ve Yüz Takibi
- Şekil ve nesne tanıma (HSV, Contours)
- Arka plan çıkarma
- Yüz/göz/eller üzerinden nesne takibi
- `mouse event` ve `eye-tracking` uygulamaları

### `klasor12/` – İleri Görüntü Teknikleri
- Görüntü karşılaştırma (template matching)
- Görüntü çözünürlüğü ayarlama
- Bulanıklaştırma, morfolojik işlemler
- Görüntü dönüşümleri

### `materyal/` – Görsel ve Video Kaynakları
- Eğitim boyunca kullanılan `.jpg` ve `.mp4` dosyaları
- Her klasöre özel örnek görsel/video içerikleri

---

## 📌 Kullanım Notları

- Her klasörde `.py` formatında örnek dosyalar yer almakta olup, doğrudan çalıştırılabilir.  
- Görsel ve video dosyaları `materyal/` klasöründe organize edilmiştir.  
- Kodlar açıklamalı ve modüler şekilde hazırlanmıştır.  

### Kurulum
Aşağıdaki komut ile gerekli kütüphaneleri yükleyebilirsiniz:

```bash
pip install opencv-python numpy

