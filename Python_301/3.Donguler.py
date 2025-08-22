# FOR
print("Cavit Batu Soylu")
print("Cavit Batu Soylu")
print("Cavit Batu Soylu")
print("Cavit Batu Soylu")

for i in range(4):
    print("{}. yazı => Bilgisayar Mühendisi".format(i+1))


# 5,6,7,8,9
for sayi in range(5,10):
    print(sayi)
    print("deneme")
    
isimler = ["Cavit","Batu","Mert","Ahmet","Selin"]

for isim in isimler:
    print(isim)
    
tup = (5.0, "ahmet",{12:"kemal"})

for eleman in tup:
    print(eleman)
#-------------------------------------------------
for karakter in 'Cavit Batu':
    print(karakter)
    
sayilar = [2,4,5,7]

for sayi in sayilar:
    print(sayi)
    
karisik = ['F', 75.8, 'Kaan', 74, True]

for eleman in karisik:
    print(eleman)
    
bilgiler = {'Cavit': 'Bilgisayar Mühendisi',
            'Batu': 'Yapay Zeka Mühendisi',
            'Nida': 'Matematik Mühendisi'}
print(bilgiler.keys())
for key in bilgiler:
    print(key)
print(bilgiler.keys())
for key in bilgiler.keys():
    print(key)
print(bilgiler.values())    
for key in bilgiler.values():
    print(key)

print(bilgiler.items())

for key, value in bilgiler.items():
    print("Adı:",key,"Mesleği:",value)
    
benzersizSayilar = {2,3,4,2,3,4,5,6,7,4,6,8}

print(benzersizSayilar)

for sayi in benzersizSayilar:
    print(sayi)
    
tupleListesi = [(21,51),(41,54),(-5,4),(-5,-9)]

for ikili in tupleListesi:
    sayi1,sayi2 = ikili
    print(ikili)
    print(sayi1*4, sayi2*4)
    
for sayi1, sayi2 in tupleListesi:
    print(sayi1*4,sayi2*4)
    
tupleListesi = [('Okan',28,1578),('Melike',35,9574)]

oyuncuNumarasi = 1
for ad, yas, puan in tupleListesi:
    print("{}. oyuncunun bilgileri: ".format(oyuncuNumarasi))
    print("Ad: ", ad)
    print("Yaş: ", yas)
    print("Puan: ", puan)
    oyuncuNumarasi += 1
#-------------------------------------------------
# Liste içerisindeki tek ve çift sayıların kaç tane olduğunu
# bulan ve bu elemanları liste içerisinde tutan programı yazınız

sayilar = [2,3,4,5,1,6,7,61,24,23,87,65,77,78,98]
tekSayilar = []
ciftSayilar = list()

for sayi in sayilar:
    if sayi % 2 == 0:
        ciftSayilar.append(sayi)
    else:
        tekSayilar.append(sayi)
        
print("Tek sayılar: {} ve {} tane tek sayı bulunmaktadır.".format(tekSayilar,len(tekSayilar)))
print("Çift sayılar: {} ve {} tane çift sayı bulunmaktadır.".format(ciftSayilar,len(ciftSayilar)))
#-------------------------------------------------
"""
1x1=1    2x1=2    ...    10x1=10
1x2=2    2x2=2    ...    10x2=20
  .        .                .
  .        .                .
  .        .                .
1x10=10  2x10=20  ...    10x10=100
"""

for i in range(1,11):
    for j in range(1,11):
        print("{}x{}={}".format(j, i, i*j), end = " ")
    print()
#-------------------------------------------------
# 1 ile 500 arasında karekökü tam sayı olan sayıları yazdıran program
from math import sqrt

for i in range(1,501):
    if int(sqrt(i)) ** 2 == i:
        print("Karekök {} = {}   {} karekökü tam sayı olan bir sayıdır!".format(i,sqrt(i),i))
#-------------------------------------------------
# For - else
sayilar = [3,7,11,27]
for sayi in sayilar:
    if sayi % 2 == 0:
        print("{} çift sayıdır.".format(sayi))
        break
else:
    print("Çift sayı bulunmamaktadır!")
#-------------------------------------------------
# For döngüsünün kullanıldığı yerler
sayilar = [3,5,7,1,-2,0,11]
sayilarinKareleri = []
for sayi in sayilar:
    sayilarinKareleri.append(sayi*sayi)
    
print(sayilarinKareleri)

sayilarinKareleri2 = [sayi*sayi for sayi in sayilar]
sayilarinKareleri2Tuple = tuple(sayi*sayi for sayi in sayilar)
print(sayilarinKareleri2)
print(sayilarinKareleri2Tuple)
sayilarinKareleriSet = set (sayi*sayi for sayi in sayilar)
print(sayilarinKareleriSet)







#%% WHİLE

# başlangıç değeri (start)
# bitiş yeri(stop)
# adım değeri(step)

#0,1,2,3,4
for i in range(5):
    print(i)
    
# initialisation
# condition
# increment/decrement

i = 1 # initialisation (ilk değer ataması)

while i <= 5:
    print(i)
    i += 1
#-------------------------------------------------
sayilar = [10,15,22,33,44,55,150,75]
index = 0 # initialisation (ilk değer ataması)

while index < len(sayilar): # condition (şart)
    print(sayilar[index])
    index += 1 # increment
print("Döngü bittikten sonra index değeri", index)
print("Tersten Yazdırma")

index = len(sayilar) - 1 # initialisation

while index >= 0:
    print(sayilar[index])
    index -= 1 # decrement
#-------------------------------------------------
sayi = 1
baslangic = sayi
bitis = 10
toplam = 0

while sayi <= bitis:
    toplam += sayi
    sayi += 1
    
print("[{}-{}] arasındaki tam sayıların toplamı: {}".format(baslangic,bitis,toplam))
print("[{}-{}] arasındaki tam sayıların toplamı: {}".format(baslangic,bitis,sum(range(baslangic,bitis+1))))
#-------------------------------------------------
baslangic = 1
i = baslangic
bitis = 100
sayi1 = 5
sayi2 = 7
sayac = 0

while i <= bitis:
    if i % sayi1 == 0 or i % sayi2 == 0:
        print(i)
        sayac += sayi1
        i += sayi1

print("{}-{} aralığında {} veya {} sayısına bölünebilen {} tane sayı vardır.".format(baslangic, bitis,sayi1,sayi2,sayac))
#-------------------------------------------------
"""
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
"""
satir = 0
satirSayisi = 5
sutunSayisi = 3
while satir < satirSayisi:
    sutun = 0
    while sutun<sutunSayisi:
        print("$",end = "")
        sutun += 1
    print()
    satir += 1
#-------------------------------------------------
# Girilen sayının sayı değerleri toplamını bulan program
# 785 => 7 + 8 + 5 = 20

sayi = int(input("Lütfen bir sayı giriniz = "))
orjSayi = sayi
sayiDegerleriToplami = 0
sayiDegerleri = []
while sayi > 0:
    sayiDegerleriToplami += sayi % 10
    sayiDegerleri.append(sayi % 10)
    sayi //= 10
    
print("{} sayısının basamkalarındaki sayılar".format(orjSayi))
sayiDegerleri.reverse()
print(*sayiDegerleri)
print(sayiDegerleri)
print("{} sayısının sayı değerleri toplamı: {} ".format(orjSayi, sayiDegerleriToplami))
print("{} sayısının sayı değerleri toplamı: {} ".format(orjSayi, sum(sayiDegerleri)))
#-------------------------------------------------
n = int(input("Faktöriyelini öğrenmek istediğiniz sayıyı giriniz: "))

if n >= 0:
    i = 1
    sonuc = 1
    while i <= n:
        sonuc *= i
        i += 1
    print("{}! = {}".format(n, sonuc))
else:
    print("Lütfen doğal sayı giriniz!")
    
#-----------------
n = int(input("Faktöriyelini öğrenmek istediğiniz sayıyı giriniz: "))
orijinalN = n
sonuc = 1

if n >= 0:
    while n > 1:
        sonuc *= n
        n -= 1
    print("{}! = {}".format(orijinalN, sonuc))
else:
    print("Lütfen doğal sayı giriniz!")

#%% BREAK, CONTİNUE, PASS ANAHTAR KELİMELERİ

sayi = 1000
while True:
    print(sayi)
    if sayi == 10000:
        break
    sayi += 1000
    
count = 0
while True:
    sayi = 1
    while True:
        print(sayi)
        if sayi == 5:
            break
        sayi += 1
    count += 1
    if count == 3:
        break

for sayi in range(1,50):
    if sayi % 5 == 0:
        continue
    print(sayi)
i = 0
while i < 5:
    if i % 2 == 1:
        i += sayi1
        continue
    i += 1
    print(i)
    
for sayi in range(1,50):
    pass
print("Başka işlemler yapacağım")

if i == 0:
    print("i 0'a eşitken bir şeyler yapılacak")
    pass
else:
    pass
#-------------------------------------------------
# Bir stringin içerisindeki karakterin indeksini bulma
isim = "Cavit Batu Soylu"
aranacakHarf = 'a'
aranacakHarf = aranacakHarf.lower()

index = 0
for karakter in isim.lower():
    #print(karakter)
    if karakter == aranacakHarf:
        print("{} harfi {}. indeksteki bulunmaktadır.".format(aranacakHarf,index))
        break
    index += 1
    
print(isim.index(aranacakHarf))
#-------------------------------------------------
isim = "Fenerbahçe"
index = 0
for harf in isim:
    print("{} harfi {}. indekste bulunmaktadır".format(harf,index))
    index += 1
    
print(isim)
print(list(enumerate(isim)))
for index, harf in enumerate(isim):
    print("{} harfi {}. indekste bulunmaktadır".format(harf,index))
    
for index, harf in enumerate("Cavit Batu".lower()):
    if harf == 'a':
        print("{} harfi {}. indekste bulunmaktadır".format(harf,index))

liste = ['a',5,True,7.5]
for index, deger in enumerate(liste):
    print(index,deger)
#-------------------------------------------------
# Kullanıcı giriş bilgilerini doğru girdiği takdirde istediği
# kadar sayı girebilmesini ve bunları küçükten büyüğe sıralayabilmesini
# sağlayan programı yazınız

# Kullanıcı adı: hesapmakinesi
# Şifre: hesap12345

username = 'hesapmakinesi'
password = 'hesap12345'

kullaniciAdiVarMi = False
sifreVarMi = False
while True:
    if not kullaniciAdiVarMi:
        _username = input("Lütfen kullanıcı adınızı giriniz = ")
    if not sifreVarMi:
        _password = input("Lütfen parolanızı giriniz = ")
    
    if username != _username:
        print("Sistemde böyle bir kullanıcı bulunmamaktadır")
    elif password != password:
        kullaniciAdiVarMi = True
        print("Parolanızı yanlış girdiniz!")
    else:
        sayiAdeti = int(input("Lütfen kaç adet sayıyı sıralamak istediğinizi giriniz"))
        sayilar = []
        for i in range(sayiAdeti):
            sayi = int(input("Lütfen {}. sayıyı giriniz".format(i+1)))
            sayilar.append(sayi)
        sayilar.sort()
        print("Girmiş olduğunuz sayıların küçükten büyüğe doğru sıralanışı: ")
        for sayi in sayilar:
            print(sayi, end = " ")
        print()
        sayilar.sort(reverse = True)
        print("Girmiş olduğunuz sayıların küçükten büyüğe doğru sıralanışı: ")
        break

#%% Banka ATM
# Kartın bir şifresi vardır. Kartın başlangıçta bakiyesi 500TL'dir. 3 defa yanlış şifre girilince
# kart bloke olacaktır. 3 defa yanlış şifre girilince kart bloke olacaktırç ATM'nin işlem menüsünde
# para çekme, para yatırma, bakiye sorgulama ve kart iade işlemleri yapılmamaktadır

_kartSifre = 12345
_bakiye = 500
sifre_sayac = 3
login = False

while True:
    if login == False:
        sifre = int(input("Şifrenizi giriniz = "))
        if sifre == _kartSifre:
            login = True
        else:
            sifre_sayac -= 1
            if sifre_sayac <= 0:
                print("Kartınız bloke olmuştur! Banka ile iletişime geçiniz")
                break
            else:
                print("Yanlış şifre! Kalan hakkınız:", sifre_sayac)
                continue  # Tekrar şifre sorması için döngü başa gider

    print("""
1.Para Çek
2.Para Yatır
3.Bakiye Sorgulama
4.Kart İade
    """)
    secim = int(input("Hangi işlemi yapmak istiyorsunuz = "))
    if secim == 1:
        miktar = int(input("Kaç TL çekmek istiyorsunuz = "))
        if _bakiye < miktar:
            print("Yeterli bakiyeniz bulunmamaktadır")
            continue
        _bakiye -= miktar
    elif secim == 2:
        miktar = int(input("Kaç TL yatırmak istiyorsunuz = "))
        _bakiye += miktar
    elif secim == 3:
        print("Bakiyeniz {} TL".format(_bakiye))
    elif secim == 4:
        print("Yine Bekleriz!")
        break
    else:
        print("Lütfen 1-4 arasında bir seçim yapın!")


              
              
              
              
              
              
              
              
              
              
              
              
              
              




  