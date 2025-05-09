import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
notlar = np.random.randint(0, 101, 1000)

print("Öğrenci Notları:\n", notlar[:10])
print("Notların Ortalaması:", np.mean(notlar))
print("En Yüksek Not:", np.max(notlar))
print("En Düşük Not:", np.min(notlar))
print("Notların Standart Sapması:", np.std(notlar))

gecenler = notlar[notlar >= 50]
gecemeyenler = notlar[notlar < 50]

print("Geçen Öğrenci Sayısı:", len(gecenler))
print("Geçemeyen Öğrenci Sayısı:", len(gecemeyenler))

plt.figure(figsize=(10, 5))
plt.hist(notlar, bins=10, edgecolor = 'black', alpha=0.7)
plt.xlabel("Not Aralığı")
plt.ylabel("Öğrenci Sayısı")
plt.title("Öğrenci Not Dağılımı")
plt.grid(True)
plt.show()

sirali_notlar = np.sort(notlar)

dusuk_dilim = sirali_notlar[:100]
yuksek_dilim = sirali_notlar[-100:]

print("En Düşük %10 Ortalaması:\n", np.mean(dusuk_dilim))
print("En Yüksek %10 Ortalaması:\n", np.mean(yuksek_dilim))
