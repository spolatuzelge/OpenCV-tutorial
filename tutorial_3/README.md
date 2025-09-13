# 🎓 OpenCV Tutorial 3 – Jupyter Notebook Serisi

Bu repo, OpenCV’nin temelinden ileri seviyeye kadar farklı konularını **Jupyter Notebook** ortamında ele alan örnekleri içermektedir. Her klasör, belirli bir konuya odaklanmakta ve adım adım uygulamalı kod örnekleriyle desteklenmektedir.  

> 📌 Bu seri, OpenCV öğrenimini görselleştirmek için Jupyter tabanlı hazırlanmıştır. Kodların çıktıları doğrudan hücreler içinde görülebilir.

---

## 📂 Klasörler ve İçerikler

### 🔹 `klasor1/`
**OpenCV’ye Giriş**
- `openCVGiris.ipynb` → OpenCV kütüphanesine giriş, temel fonksiyonların tanıtımı  
- `materyal/` → Görseller ve test için kullanılan medya dosyaları  

---

### 🔹 `klasor2_1/`
**Temel Görüntü İşlemleri**
- `gorselOkuma.ipynb` → Görüntü okuma  
- `gorselGoruntuleme.ipynb` → Görüntü görüntüleme  
- `gorselYazma.ipynb` → Görüntü kaydetme  
- `colorSpace.ipynb` → Renk uzayı dönüşümleri (BGR ↔ GRAY ↔ HSV)  
- `gorsellerdeAritmetik_Islemler.ipynb` → Aritmetik işlemler (toplama, çıkarma, maskeleme)  
- `goruntulerdeAritmetik_Islemler2.ipynb` → İleri aritmetik işlemler  

---

### 🔹 `klasor2_2/`
**Görüntü İşleme Teknikleri**
- `goruntuAdaptiveEsikleme.ipynb` → Adaptif eşikleme  
- `goruntuAnalizi_Histogram.ipynb` → Histogram analizi  
- `goruntuArkaPlanCikarma.ipynb` → Arka plan çıkarma  
- `goruntuAsindirma.ipynb` → Erozyon işlemleri  
- `goruntuBasitEsikleme.ipynb` → Basit threshold teknikleri  
- `goruntuBilateralFiltre.ipynb` → Bilateral filtreleme  
- `goruntuBulaniklastirma.ipynb` → Blur işlemleri  
- `goruntuGrabcut.ipynb` → GrabCut ile nesne çıkarımı  
- `goruntuGriTonlama.ipynb` → Gri tonlama dönüşümü  
- `goruntuGurultuGiderme.ipynb` → Gürültü temizleme  
- `goruntuInpainting.ipynb` → Inpainting ile kayıp alan doldurma  
- `goruntuKenarlikOlusturma.ipynb` → Görüntü kenarlık işlemleri  
- `goruntuKonturKoordinatlari.ipynb` → Kontur çıkarımı ve koordinatlar  
- `goruntuMorfolojikIslemlerClosing.ipynb` → Morfolojik closing  
- `goruntuMorfolojikIslemlerOpening.ipynb` → Morfolojik opening  
- `goruntuMorfolojikIslemlerGradient.ipynb` → Gradient tabanlı morfolojik işlemler  
- `goruntuOtsuEsikleme.ipynb` → Otsu thresholding  
- `goruntuRenkliResiyi.ipynb` → Renkli görüntü işlemleri  
- `goruntuResize.ipynb` → Görüntü yeniden boyutlandırma  
- `goruntuSegmentasyonMorfoloji.ipynb` → Morfoloji tabanlı segmentasyon  
- `goruntuYogunlukDonusumu.ipynb` → Yoğunluk dönüşümleri  
- `goruntudeKenarSaptama.ipynb` → Kenar tespiti  

---

### 🔹 `klasor2_3/`
**Köşe ve Nesne Tespiti**
- `goruntudeHarrisKoseTespiti.ipynb` → Harris köşe tespiti  
- `goruntudeKoseTespiti.ipynb` → Genel köşe tespiti  
- `goruntudeShiTomasiKoseTespiti.ipynb` → Shi-Tomasi yöntemi ile köşe tespiti  
- `goruntudeYuvarlakNesneTespiti.ipynb` → Yuvarlak nesne tespiti  

---

## ⚙️ Gereksinimler

- Python 3.x  
- Jupyter Notebook  
- OpenCV (`opencv-python`)  
- NumPy  

Kurulum için:
```bash
pip install opencv-python numpy jupyter
