import pandas as pd

data = pd.DataFrame({
    "Yas": [25, 45, 30, 35, 40],
    "Cinsiyet": ["K", "E", "K", "E", None],
    "Maas": [6000, 8000, None, 9000, 7500],
    "Deneyim": [2, 20, 5, 10, 15],
    "Departman": ["IT", "HR", "Yönetim", "Muhasebe", "Yönetim"],
    "Terfi": [0, 1, 0, 1, 0],
})

print("Veri Setinin İlk 5 Satırı:")
print(data.head())

print("Eksik Değerlerin Sayisi:")
print(data.isnull().sum())

print("Veri Setinin Bilgisi:")
print(data.info())

print("İstatistiksel Özet:")
print(data.describe())