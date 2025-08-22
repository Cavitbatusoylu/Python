# -*- coding: utf-8 -*-

yas = int(input("Lütfen yaşınızı girin: "))

if yas < 18:
    print("Reşit değilsiniz!")
else:
    print("Reşitsiniz!")

if yas >= 18:
    print("Reşitsiniz!")
else:
    print("Reşit değilsiniz!")
    
sayi = 19

# type casting 0 dışındaki her sayının
# boolean değeri True

# sayi % 2 ==> 1
# sayi % 2 ==> 0

if sayi % 2:
    print("{} sayısı tektir!".format(sayi))
else:
    print("{} sayısı çifttir!".format(sayi))

#%% İç İçe (Nested) Koşullu İfadeler ve Örnekler

# Vizesi %40 etkili finale % 60 etkili
# Ortalaması 50 ve üzeri olursa dersi geçiyor

vize = 100
final = 49

if final >= 50:
    ort = vize * 0.4 + final * 0.6
    if ort >= 50:
        print("{} Ortalamayla Dersi Geçtiniz!".format(ort))
    else:
        print("{} Ortalamayla Dersten kaldınız!".format(ort))
else:
    print("Dersten kaldınız!")
#-------------------------------------------------------------
ay = input("Lütfen ay ismi giriniz: ")

if ay == "aralık" or ay == "ocak" or ay == "şubat":
    print("{} kış mevsimine aittir.".format(ay))
if ay == "mart" or ay == "nisan" or ay == "mayıs":
    print("{} ilkbahar mevsimine aittir.".format(ay))
if ay == "haziran" or ay == "temmuz" or ay == "ağustos":
    print("{} yaz mevsimine aittir.".format(ay))
if ay == "eylül" or ay == "ekim" or ay == "kasım":
    print("{} sonbahar mevsimine aittir.".format(ay))
else:
    print("Girdiğiniz ay bilgisi yanlıştır!")
#-------------------------------------------------------------
# Cinsiyet ve boy uzunluğuna göre mülakatı geçme durumu örneği
# Pilotluk sınavında adayların ilk aşamayı geçebilmesi için bir
# ön koşul koyulmuştur. Bu koşul:
    # Cinsiyeti KADIN olanları 1.60
    # Cinsiyeti ERKEK olanları 1.70 boy sınırını geçtiği takdirde
    # ön sağlık muayenesini geçebilirler.
    # İlgili programı yazınız.
cinsiyet = "kadın"
boy = 160
      
if (cinsiyet == "kadın" or cinsiyet == "erkek") and (boy > 20 and boy < 300):
    if cinsiyet == "kadın" and boy >= 160:
        print("Ön sağlık kontrolünü geçtiniz")
    elif cinsiyet == "erkek" and boy >= 170:
        print("Ön sağlık kontrolünü geçtiniz")
    else:
        print("Ön sağlık kontrolünden elendiniz")
else:
    print("Cinsiyeti erkek ya da kadın olarak,"
          "boyu da [20,300] cm aralığında giriniz")
#-------------------------------------------------------------
# Kullanıcıdan 3 tane sayı alan ve bu 3 sayıdan en büyük ve en küçük
# değeri söyleyen programı yazınız
sayi1, sayi2, sayi3 = int(input("Lütfen 1.sayıyı giriniz")),
int(input("Lütfen 2.sayıyı giriniz")),int(input("Lütfen 3.sayıyı giriniz"))
print(sayi1,sayi2,sayi3)
buyuk = sayi1
kucuk = sayi1

if sayi1 < sayi2 or sayi1 < sayi3:
    buyuk = sayi2
    if sayi2 < sayi3:
        buyuk = sayi3
        
if sayi1 > sayi2 or sayi1 > sayi3:
    kucuk = sayi2
    if sayi2 > sayi3:
        kucuk = sayi3
        
print("{} {} {} sayıları arasından küçük olanı {}".format(sayi1,sayi2,sayi3,kucuk))
print("{} {} {} sayıları arasından büyük olanı {}".format(sayi1,sayi2,sayi3,buyuk))
        
sayilar = [sayi1,sayi2,sayi3]
print("{} {} {} sayıları arasından küçük olanı {}".format(sayi1,sayi2,sayi3,kucuk))
print("{} {} {} sayıları arasından büyük olanı {}".format(sayi1,sayi2,sayi3,buyuk))
#-------------------------------------------------------------
# Kullanıcı adı ve şifre kontrolü yapan program
admin_username = "admin123"
admin_password = "pass123"

kullaniciAdi = input("Lütfen kullanıcı adınızı giriniz")
kullaniciSifre = input("Lütfen şifrenizi giriniz") 
        
if kullaniciAdi == admin_username and kullaniciSifre == admin_password:
    print("Sisteme başarılı bir şekilde giriş yaptınız!")
elif kullaniciAdi == admin_username:
    print("Lütfen şifrenizi doğru giriniz!")
elif kullaniciSifre == admin_password:
    print("Lütfen kullanıcı adınızı doğru giriniz!")
else:
    print("Lütfen kullanıcı adınızı ve şifrenizi doğru giriniz.")
#-------------------------------------------------------------
# Üçgen bilgisini söyleyen program
kenar1,kenar2,kenar3 = int(input("Lütfen 1.kenarı giriniz")),
int(input("Lütfen 2.kenarı giriniz")),int(input("Lütfen 3.kenarı giriniz"))

# absolute value - mutlak değer
if abs(kenar1-kenar2) < kenar3 and kenar3 < kenar1 + kenar2:
    if kenar1 == kenar2 and kenar1 == kenar3:
        print("Eşkenar Üçgen")
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
        print("İkizkenar Üçgen")
    else:
        print("Çeşitkenar Üçgen")
else:
    print("Bu 3 kenar bilgisiyle üçgen çizilemez!")
    
#%% ASCII Tablosu
#A-Z 65-90  # 26 Harf
#a-z 97-122 # 26 Harf
harf = input("Lütfen bir har giriniz: ")

# print(harf)
if len(harf) == 1:
    if ord(harf) >= 65 and ord(harf) <= 90:
        print("{} büyük harftir!".format(harf))
    elif ord(harf) >= 97 and ord(harf) <122:
        print("{} küçük harftir!". format(harf))
    else:
        print("Girdiğiniz karakter latin alfabesinde bulunamamaktadır")
else:
    print("Lütfen sadece 1 karakter giriniz!")

print(ord("ç"))
print(ord("ö"))
print(ord("ğ"))
print(ord("İ"))




























