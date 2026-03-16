import numpy as np
import matplotlib.pyplot as plt

veri = np.load(r'C:\Users\suley\OneDrive\Masaüstü\Features.npz', allow_pickle=True)
tum_ozellikler = veri['Features'] 

islem_goren_veri = tum_ozellikler[:, :100, :]

en_kucuk = np.min(islem_goren_veri)
en_buyuk = np.max(islem_goren_veri)
normalize_veri = (islem_goren_veri - en_kucuk) / (en_buyuk - en_kucuk)

gercek_kisi_skorlari = []  
sahte_kisi_skorlari = [] 

ornek_sayisi = 10
kisi_sayisi = 100

print("Dosya içindekiler:", veri.files)
print("Orijinal veri boyutu:", tum_ozellikler.shape)
print("İşlem yapılacak boyut:", islem_goren_veri.shape)
print("Normalizasyon sonrası min:", np.min(normalize_veri))
print("Normalizasyon sonrası max:", np.max(normalize_veri))

for kisi in range(kisi_sayisi):
    for i in range(ornek_sayisi):
        for j in range(i + 1, ornek_sayisi):
            vektor1 = normalize_veri[i, kisi, :]
            vektor2 = normalize_veri[j, kisi, :]

            mesafe = np.linalg.norm(vektor1 - vektor2)
            skor = 1 / (1 + mesafe)
            gercek_kisi_skorlari.append(skor)

for kisi1 in range(kisi_sayisi):
    for kisi2 in range(kisi1 + 1, kisi_sayisi):
        for i in range(ornek_sayisi):
            for j in range(ornek_sayisi):
                vektor1 = normalize_veri[i, kisi1, :]
                vektor2 = normalize_veri[j, kisi2, :]
                
                mesafe = np.linalg.norm(vektor1 - vektor2)
                skor = 1 / (1 + mesafe)
                sahte_kisi_skorlari.append(skor)


gercek_kisi_skorlari = np.array(gercek_kisi_skorlari)
sahte_kisi_skorlari = np.array(sahte_kisi_skorlari)

print("Hesaplanan Gerçek (Genuine) skor sayısı:", len(gercek_kisi_skorlari))
print("Hesaplanan Sahte (Imposter) skor sayısı:", len(sahte_kisi_skorlari))


esik_degerleri = np.linspace(0, 1, 1000)
far_listesi = []
frr_listesi = []

for esik in esik_degerleri:

    far = np.sum(sahte_kisi_skorlari >= esik) / len(sahte_kisi_skorlari)
    far_listesi.append(far)

    frr = np.sum(gercek_kisi_skorlari < esik) / len(gercek_kisi_skorlari)
    frr_listesi.append(frr)

far_listesi = np.array(far_listesi)
frr_listesi = np.array(frr_listesi)


farklar = np.abs(far_listesi - frr_listesi)
en_yakin_indis = np.argmin(farklar)
eer_orani = (far_listesi[en_yakin_indis] + frr_listesi[en_yakin_indis]) / 2
ideal_esik = esik_degerleri[en_yakin_indis]

print(f"EER: % {eer_orani * 100:.2f} (İdeal Eşik Değeri: {ideal_esik:.4f})")

fig, (grafik1, grafik2, grafik3) = plt.subplots(3, 1, figsize=(8, 12))


grafik1.hist(gercek_kisi_skorlari, bins=50, alpha=0.7, color='dodgerblue', label='Doğru Kişi', density=True)
grafik1.hist(sahte_kisi_skorlari, bins=50, alpha=0.7, color='darkorange', label='Sahtekar', density=True)
grafik1.set_title("Skor Dağılımı")
grafik1.set_xlabel("Eşleşme Skoru")
grafik1.set_ylabel("Yoğunluk")
grafik1.legend()


grafik2.plot(esik_degerleri, far_listesi, label='FAR (Yanlış Kabul)', color='purple', linewidth=2)
grafik2.plot(esik_degerleri, frr_listesi, label='FRR (Yanlış Red)', color='c', linewidth=2)

grafik2.plot(ideal_esik, eer_orani, 'k*', markersize=10, label=f'EER (% {eer_orani*100:.2f})')
grafik2.set_title("Eşik Değerine Göre FAR ve FRR Değişimi")
grafik2.set_xlabel("Eşik Değeri (Threshold)")
grafik2.set_ylabel("Hata Oranı")
grafik2.legend()


grafik3.plot(far_listesi, frr_listesi, color='crimson', linewidth=2)
grafik3.plot(eer_orani, eer_orani, 'k*', markersize=10, label=f'EER (% {eer_orani*100:.2f})')
grafik3.set_title("FAR & FRR Karşılaştırması")
grafik3.set_xlabel("FAR")
grafik3.set_ylabel("FRR")
grafik3.legend()

plt.tight_layout()
plt.subplots_adjust(hspace=0.5, bottom=0.1)


fig.text(0.5, 0.02, "https://github.com/Muratsuleymanoglu/Biyometrik-Sistemler.git", 
         ha="center", va="center", fontsize=11, color="black",
         bbox=dict(facecolor='lightyellow', edgecolor='orange', boxstyle='round,pad=0.5', alpha=0.9))

plt.savefig("biyometri_odev_grafikleri.pdf", format="pdf", bbox_inches="tight")
plt.show()