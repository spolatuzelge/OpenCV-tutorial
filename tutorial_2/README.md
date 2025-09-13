# 🎓 OpenCV Python Eğitim Notları

Bu repo, OpenCV’nin temelinden ileri seviyeye kadar farklı konularını adım adım ele alan Python örnek dosyalarını içermektedir. Çalışmalar, Udemy eğitim serisi ve ek kaynaklardan esinlenerek hazırlanmış olup; her dosya belirli bir konuya odaklanmaktadır.

> 🧠 Kodlar öğrenme ve pratik amaçlıdır. Her bölüm, konunun teorisini pekiştiren örneklerle desteklenmiştir.  

---

## 📂 Repo Yapısı

### 🔹 `201`
**Temel Görüntü ve Video İşlemleri**
- `01_ResimYukleme.py` → Görüntü yükleme ve gösterme  
- `02_RGB_to_GRAY.py` → Renkli görüntüyü gri tonlamaya çevirme  
- `03_resimOlusturma.py` → Yeni görüntü oluşturma  
- `04_pikselDegeriOkumaVEdegistirme.py` → Piksel değerlerine erişim ve değiştirme  
- `05_iki_resmiBirlestirme.py` → Görüntü birleştirme  
- `06_istatistikselBilgiAlma_treshold.py` → İstatistiksel bilgi alma ve threshold işlemleri  
- `07_pikselNormalizasyonu.py` → Piksel normalizasyonu  
- `08_videoOkuma_Gosterme_Kaydetme.py` → Video okuma, gösterme, kaydetme  
- `09_goruntuCevirme.py` → Görüntü dönüştürme işlemleri  
- `10_geometrik_sekiller_olusturmak.py` → Çizgi, dikdörtgen, çember çizimi  
- `11_tresholding.py` → Threshold teknikleri  
- `12_kameraGoruntusu_TerslemeBlurKenarBulma.py` → Kamera verisi üzerinde tersleme, bulanıklaştırma, kenar bulma  

---

### 🔹 `301`
**Renk Uzayı, Histogram ve Kenar Algılama**
- `01_renkUzayininDegistirilmesi.py` → Renk uzayı dönüşümleri (BGR ↔ HSV vb.)  
- `03_roi.py` → Region of Interest (ROI) işlemleri  
- `04_histogramOlusturmak.py` → Histogram oluşturma  
- `05_histogramEsitleme.py` → Histogram eşitleme  
- `06_histogramKarsilastirma.py` → Histogram karşılaştırma  
- `07_gaussDuzlestirmeFiltresi.py` → Gauss filtreleme  
- `08_kenarKoruyanFiltrelemeALGO.py` → Kenar koruyan filtreleme algoritması  
- `09_sobelFiltresi.py` → Sobel filtresi ile kenar çıkarımı  
- `10_cannyKenarTespiti.py` → Canny kenar tespiti  
- `11_otsuEsikTresh.py` → Otsu thresholding  
- `12_goruntuKonturlari.py` → Kontur çıkarımı  
- `13_hoffmanCizgiTESP.py` → Hough doğrusal tespiti  
- `14_hoffmanOlasiliksal.py` → Probabilistik Hough doğrular  

---

### 🔹 `401`
**İleri Görüntü İşleme Teknikleri**
- `01_resmeGurultuEkleme.py` → Gürültü ekleme  
- `02_goruntuKeskinlestirme.py` → Görüntü keskinleştirme  
- `03_koseSaptama_HARRiS.py` → Harris köşe tespiti  
- `04_shiTomas_koseSaptama.py` → Shi-Tomasi köşe tespiti  
- `05_subPixel_koseSaptama.py` → Sub-pixel köşe tespiti  
- `06_HOG_yayaTespiti.py` → HOG tabanlı yaya tespiti  
- `07_templateMatching_NesneTespiti.py` → Template matching ile nesne tespiti  

---

### 🔹 `501`
**Nesne Tanıma ve Sınıflandırma**
- `01_QR-detec.py` → QR kod tespiti  
- `02_DNNGoruntuSiniflandirma.py` → Derin sinir ağları ile görüntü sınıflandırma  

---

## ⚙️ Gereksinimler

- Python 3.x  
- OpenCV (`opencv-python`)  
- NumPy  

Kurulum için:
```bash
pip install opencv-python numpy

