# Biyometrik-Sistemler

Bu proje, Bartın Üniversitesi Bilgisayar Mühendisliği bölümü "BSM361 Biyometrik Sistemler"  dersi kapsamında geliştirilmiş bir biyometrik sistem başarım değerlendirme (performans analizi) uygulamasıdır. 

## 📌 Proje Özeti
Bir biyometrik sistemin özellik çıkaran modülünden  elde edilen veriler kullanılarak eşleştirme algoritmaları yazılmış ve sistemin performans metrikleri grafiksel olarak analiz edilmiştir.Sistem, 100 farklı kullanıcıya ait özellikleri işleyerek Gerçek ve Sahteci skor dağılımlarını oluşturmaktadır.

## ⚙️ Özellikler ve Hesaplamalar
**Veri Hazırlama:** `Features.npz` dosyasından okunan biyometrik verilerin ilk 100 kişiye ait olan kısmı (her biri 6 elemanlı 10 örneklem) ayrıştırılmış ve değerler 0-1 aralığında kalacak şekilde normalize edilmiştir.
**Skor Hesaplama:** İki özellik vektörü arasındaki mesafe Öklid yöntemiyle bulunmuş ve eşleşme skoru $1 / (1 + \text{Öklid Mesafesi})$ formülü ile hesaplanmıştır.

**Performans Metrikleri:**
  * Eşik değerlerine göre **Yanlış Kabul Oranı (FAR)** ve **Yanlış Ret Oranı (FRR)** hesaplanmıştır.
  * Sistemin optimum çalışma noktasını gösteren **Eşit Hata Oranı (EER)** tespit edilmiştir.

## 📊 Grafikler ve Çıktılar
Proje çalıştırıldığında sistem performansını özetleyen üç ana grafik üretilir ve tek bir PDF dosyası olarak kaydedilir:
1. **Skor Dağılımları:** Gerçek ve sahteci skorların yoğunluk histogramı.
2. **FAR ve FRR Değişimi:** Eşik değerlerine karşılık gelen hata oranları ve EER noktası.
3. **FAR vs FRR Karşılaştırması:** Sistem hatalarının birbirine göre değişim eğrisi.

## 💻 Kullanılan Teknolojiler
* **Python 3**
* **NumPy:** Vektörel işlemler, uzaklık hesaplamaları ve normalizasyon.
* **Matplotlib:** Veri görselleştirme ve PDF formatında çıktı alma.
