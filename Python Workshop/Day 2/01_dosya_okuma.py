# "demo.txt" adında bir dosya oluşturur, eğer zaten varsa hata verir.
open("demo.txt", "x")

# "w" modu ile dosya açılır. İçeriği varsa silinir, üzerine yeni içerik yazılır.
with open("demo.txt", "w") as dosya:
    dosya.write("Merhaba Python\n")  # İlk satır yazılır
    dosya.write("Python Workshop\n")  # İkinci satır yazılır

# "a" modu ile dosyaya ekleme yapılır, mevcut içerik silinmez.
with open("demo.txt", "a") as dosya:
    dosya.write("Selam!\n")  # Üçüncü satır
    dosya.write("İyiyim\n")  # Dördüncü satır

# "r" modu ile dosya okunur, tüm içerik tek seferde alınır.
with open("demo.txt", "r") as dosya:
    veri = dosya.read()
    print(veri)  # İçerik ekrana yazdırılır

# Satır satır okuma (liste olarak)
with open("demo.txt", "r") as dosya:
    satirlar = dosya.readlines()
    print(satirlar)  # 'veri' yerine 'satirlar' yazılmalıydı

# Dosyayı satır satır okuyup, boşluk ve \n gibi karakterleri temizleyerek yazdırır
with open("demo.txt", "r") as dosya:
    for satir in dosya:
        print(satir.strip())  # İndent hatası düzeltilip satır temizlendi

# Kullanıcıdan bir not alınıp "notlar.txt" dosyasına eklenir
not_ = input("Notunuzu giriniz: ")
with open("notlar.txt", "a") as dosya:
    dosya.write(not_ + "\n")

print("Notunuz kaydedildi.")

# Hata yakalama örneği: Dosya yoksa kullanıcıya mesaj verilir
try:
    with open("olmayan_dosya.txt", "r") as dosya:
        icerik = dosya.read()  # 'print =' yerine doğru değişken atanmalıydı
        print(icerik)
except FileNotFoundError:
    print("Dosya bulunamadı.")
