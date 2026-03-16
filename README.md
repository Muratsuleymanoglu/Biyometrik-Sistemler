# Biyometrik-Sistemler

[cite_start]Bu proje, Bartın Üniversitesi Bilgisayar Mühendisliği bölümü [cite: 2, 10] [cite_start]"BSM361 Biyometrik Sistemlere Giriş" [cite: 12, 14] dersi kapsamında geliştirilmiş bir biyometrik sistem başarım değerlendirme (performans analizi) uygulamasıdır. 

## 📌 Proje Özeti
Bir biyometrik sistemin özellik çıkaran modülünden (Feature Extractor) elde edilen veriler kullanılarak eşleştirme algoritmaları yazılmış ve sistemin performans metrikleri grafiksel olarak analiz edilmiştir. [cite_start]Sistem, 100 farklı kullanıcıya ait özellikleri işleyerek [cite: 36] [cite_start]Gerçek (Genuine) ve Sahteci (Imposter) skor dağılımlarını [cite: 41, 42] oluşturmaktadır.

## ⚙️ Özellikler ve Hesaplamalar
* [cite_start]**Veri Hazırlama:** `Features.npz` dosyasından okunan biyometrik verilerin ilk 100 kişiye ait olan kısmı (her biri 6 elemanlı 10 örneklem) ayrıştırılmış ve değerler 0-1 aralığında kalacak şekilde normalize edilmiştir[cite: 36, 38].
* [cite_start]**Skor Hesaplama:** İki özellik vektörü arasındaki mesafe Öklid (Euclidean) yöntemiyle bulunmuş ve eşleşme skoru $1 / (1 + \text{Öklid Mesafesi})$ formülü ile hesaplanmıştır[cite: 39].
* **Performans Metrikleri:**
  * [cite_start]Eşik (threshold) değerlerine göre **Yanlış Kabul Oranı (FAR)** ve **Yanlış Ret Oranı (FRR)** hesaplanmıştır[cite: 44, 45].
  * [cite_start]Sistemin optimum çalışma noktasını gösteren **Eşit Hata Oranı (EER)** tespit edilmiştir[cite: 46].

## 📊 Grafikler ve Çıktılar
Proje çalıştırıldığında sistem performansını özetleyen üç ana grafik üretilir ve tek bir PDF dosyası olarak kaydedilir:
1. [cite_start]**Skor Dağılımları:** Gerçek ve sahteci skorların yoğunluk histogramı[cite: 43].
2. [cite_start]**FAR ve FRR Değişimi:** Eşik değerlerine karşılık gelen hata oranları ve EER noktası[cite: 47].
3. [cite_start]**FAR vs FRR Karşılaştırması:** Sistem hatalarının birbirine göre değişim eğrisi[cite: 48].

## 💻 Kullanılan Teknolojiler
* **Python 3**
* **NumPy:** Vektörel işlemler, uzaklık hesaplamaları ve normalizasyon.
* **Matplotlib:** Veri görselleştirme ve PDF formatında çıktı alma.

## 🚀 Kurulum ve Kullanım
Projeyi kendi bilgisayarınızda çalıştırmak için:

1. Depoyu klonlayın:
   ```bash
   git clone [https://github.com/Muratsuleymanoglu/Biyometrik-Sistemler.git](https://github.com/Muratsuleymanoglu/Biyometrik-Sistemler.git)
