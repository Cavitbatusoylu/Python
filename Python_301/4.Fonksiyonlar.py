# -*- coding: utf-8 -*-

# definition (tanımlama)

def seslen():
    print("Sesleniyorum")
    print("Naber")
    print("Nasılsın")
    print("Seslenmeyi bitirdim")
    
seslen()
seslen()
seslen()
seslen()
seslen()
seslen()
print(type(seslen))
print(seslen)

# call - çağırma
# invoke
seslen()

#%% Parametresiz Fonksiyonlar
def isimSoyle():
    print("Cavit Batu Soylu")
    
def bilgileriSoyle():
    isimSoyle()
    print("Van Yüzüncü Yıl Üniversitesi")
    print("Bilgisayar Mühendisliği")
    print("Tuşba/Van")
    
bilgileriSoyle()
bilgileriSoyle()
bilgileriSoyle()
bilgileriSoyle()
bilgileriSoyle()

for i in range(10):
    isimSoyle()

#%% Parametreli Fonksiyonlar
def bilgiVer():
    print("Cavit Batu Soylu")

def topla(sayi1,sayi2):
    print("Sayı1: {} Sayı2: {} Toplam: {}".format(sayi1,sayi2,topla))

topla(11,25)
topla(19,27)

def isimSoyle(isim):
    print("Kulllanıcı Bilgisi:", isim)
    
isimSoyle("Cavit Batu Soylu")
isimSoyle("Kazım Mert Karaca")
isimSoyle("Selim Acar")

#%% return
def bilgiVer1():
    print("Cavit Batu Soylu")
bilgiVer1()

# overriding - geçersiz kılmak
def bilgiVer2(isim):
    print(isim)
    return "Kişiyle ilgili bilgi verildi"
bilgiVer2("Kazım Mert Karaca")

sayi = 10
print(sayi)
sayi = 20
print(sayi)
urun = bilgiVer2("Selim Kapı")
print(urun)

def carp(sayi1, sayi2):
    return sayi1 * sayi2
print(45)
print(carp(5,9))

def topla(sayi1, sayi2):
    print("Toplama sonucu = ", sayi1 + sayi2)
    return sayi1 + sayi2
topla(75,147)
#print(topla(75,147))

#---------------------------------------------
def mutlakDegerliCarpim(sayi1, sayi2):
    return abs(sayi1*sayi2)
print(mutlakDegerliCarpim(-5, -6) * 3)
print(mutlakDegerliCarpim(5, -6) / 5)
print(mutlakDegerliCarpim(5, 6) * 5)


def ucgeninKenarlariniSoyle(k1, k2, k3):
    return "Kenar1 : {}".format(k1), "Kenar2 : {}".format(k2), "Kenar3 : {}".format(k3)
print(ucgeninKenarlariniSoyle(3, 4, 5))

bilgi1, bilgi2, bilgi3 = ucgeninKenarlariniSoyle(3, 4, 5)
print(bilgi1)
print(bilgi2)
print(bilgi3)

from math import pi

def daireAlanVeCevreHesapla(r):
    return[pi * r * r,2 * pi * r]

def daireAlanVeCevreBilgiVer(cevreVeAlan):
    print("Dairenin Alanı = ",cevreVeAlan[0])
    print("Dairenin Çevresi = ",cevreVeAlan[1])

alan, cevre = daireAlanVeCevreHesapla(5)
daireAlanVeCevreBilgiVer(daireAlanVeCevreHesapla(5))
daireAlanVeCevreBilgiVer([alan,cevre])
daireAlanVeCevreBilgiVer([alan,cevre])

#%% PASS BY VALUE (Değer Geçişi)
#   PASS BY REFERENCE (Adres Geçişi)

sayi1 = 10
sayi2 = sayi1
print(sayi1, sayi2)
sayi1 = 20
print(sayi1, sayi2)

liste1 = [10,20,30]
liste2 = liste1
print(liste1, liste2)
liste1[0] = 75
print(liste1, liste2)

def guncelle(sayi):
    print("sayi id", id(sayi))
    sayi = 9
    print("sayi id", id(sayi))
    print("Func Sayi",sayi)
    
sayimiz = 20
print("Sayimiz id",id(sayimiz))
print("Sayimiz deger", sayimiz)
guncelle(sayimiz)
print("Guncelledikten sonra sayimizin degeri", sayimiz)

def listeGuncelle(liste):
    print("Func liste id: ", id(liste))
    liste[0] = 1000
    print("Func liste id: ",id(liste))
    
listemiz = [0,10,20,30]
print("Listemiz id: ",id(listemiz))
listeGuncelle(listemiz)
print(listemiz)

#%% Types of Arguments (Argüman tipleri)
# Positional, keyword, default, variable length

def topla(s1,s2=0):
    print("s1:{},s2:{}".format(s1,s2))
    return s1+s2

print(topla(10,20))
print(topla(50))
print(topla(s2 = 150, s1 = 100))

def topla(s1, s2, *args, **kwargs):
    print(s1,s2,args)
    print(kwargs)
    if kwargs['islem'] == '+':
        print("Yapılan işlem toplama işlemidir!")
        print(s1+s2+sum(args))
    else:
        print("Bu fonksiyon toplama işlemi dışında bir işlem yapmamaktadır")
topla(2,3,4,5,6,1,7,9,10,75,95, islem = "*")

#%% Positional Arguments (Konumu Belli Argümanlar)

# single entry single exit
def hesapla(s1,s2,islem):
    sonuc = None
    if islem == '+':
        sonuc = s1 + s2
    elif islem == '-':
        sonuc = s1 - s2
    elif islem == '*':
        sonuc = s1 * s2
    elif islem == '/':
        sonuc = s1 / s2
    elif islem == '%':
        sonuc = s1 % s2
    else:
        sonuc = "5 temel dışında hesaplama yapılamamaktadır"
    return sonuc        

print(hesapla(74,15,'+'))
print(hesapla(74,15,'-'))
print(hesapla(74,15,'*'))
print(hesapla(74,15,'/'))
print(hesapla(74,15,'%'))
print(hesapla(74,15,'//'))

#%% Keyword ve Default Arguments

def ogrenciBilgiSoyle(isim, numara, adres = "", sube = ""):
    print("Öğrencinin ismi: ", isim)
    print("Öğrencinin numara: ", numara)
    if adres != "":
        print("Öğrencinin adresi = ",adres)
    if sube != "":
        print("Öğrencinin şubesi = ",sube)
        
ogrenciBilgiSoyle("Cavit", 197, "Tuşba/Van", "A")
ogrenciBilgiSoyle("Batu", 198)
ogrenciBilgiSoyle("Mert", 199, sube = "E")    

ogrenciBilgiSoyle(sube = 'A', adres = "Tuşba/Van", isim = "Enes",numara = 200)

ogrenciBilgiSoyle("Kemal", 201, sube = "F", adres = "Levent/İstanbul")

#%% Variable - Length Arguments

# * keyword'ü olmayan argümanları tutar. (*args)
# ** ise keyword'ü olan argümanları tutar. (**kwargs)

def bilgileriGoster(isim, cavit = "", *args, **kwargs):
    print("Positional Argument",isim)
    print("Positional Argument",cavit)
    print(args)
    print(kwargs)
    
bilgileriGoster("Cavit", "Batu", "Aliye",
                batu = 29, aliye = 36)
help(print)

#---------------------------------------------
from math import sqrt
def karekokHesapla(*args):
    liste = []
    for sayi in args:
        #print(round(sqrt(sayi),4))
        liste.append(round(sqrt(sayi),4))
    return liste    
    
karekokHesapla(5,7,9,16,25,34)

#%% Local (Yerel) ve Global Kavramı

sayi = 10

def func1():
    global sayi
    sayi = 20
    print("Local sayi: ", sayi, "Adres: ",id(sayi))
    
print("Global sayi: ", sayi, "Adres: ", id(sayi))

if True:
    y = 50
print(y)

while True:
    z = 100
    break
print(z)

isim = "Cavit"
print(globals()['isim'])
print(globals()['y'])
print(globals()['z'])
print(globals(['sayi']))

#%% Recursive ve Iterative Fonksiyonlar

def iterFunc(sayi):
    for i in range(sayi, -1, -1):
        print(i)
        
iterFunc(20)

def recFunc(sayi):
    if sayi == -1:
        return None
    print(sayi)
    recFunc(sayi-1)
    
recFunc(20)

#---------------------------------------------
def iterFact(n):
    sonuc = None
    if type(n) == int and n >= 0:
        sonuc = 1
        for i in range(2,n+1):
            sonuc *= i
        return sonuc
    else:
        return "Lütfen doğal sayı giriniz"
    
print(iterFact(5))
print(iterFact(6))
print(iterFact(-1))
print(iterFact(1.5))

def recFact(n):
    if type(n) == int and n >= 0:
        if n == 0:
            return 1
        return n * recFact(n-1)
    else:
        return "Lütfen doğal sayı giriniz!"
    
print(recFact(5))
print(recFact(6))
print(recFact(-1))
print(recFact(1.5))

#%% Lambda Anonymous Functions (İsimleri Olmayan Fonksiyonlar)

def kareAl(sayi):
    return sayi * sayi

print(type(kareAl))
print(kareAl(5))

lambdaKareAl = lambda sayi:sayi * sayi

print(type(lambdaKareAl))
print(lambdaKareAl(5))

lambdaTopla = lambda sayi1,sayi2:sayi1 + sayi2
print(lambdaTopla(10.2,17.7))
      
fullName = lambda name, surname:name + " " + surname
print(fullName("Cavit Batu","Soylu"))

#---------------------------------------------
kupAl = lambda sayi : sayi * sayi * sayi
kupAl2 = lambda s : s**3

print(kupAl(4))
print(kupAl2(4))

tersYaz = lambda string:string[::-1]
print(tersYaz("Cavit"))

#%% Özel Fonksiyonlara Giriş  filter()  map()  reduce()
# filter()
sayilar = [3, 2, 5, 6, -7, 14, 4, -5, -6, -5, -3, 11, 110, -15]

def pozitifMi(s):
    return s > 0

for sayi in sayilar:
    if sayi > 0:
        print(sayi)
        
print(pozitifMi(5))
print(pozitifMi(6))
print(pozitifMi(0))
print(pozitifMi(-3))

pozitifSayilar1 = list(filter(pozitifMi,sayilar))
pozitifSayilar2 = list(filter(lambda s:s > 0, sayilar))
negatifSayilar1 = list(filter(lambda s:s < 0, sayilar))
negatifSayilar2 = [sayi for sayi in sayilar if sayi not in pozitifSayilar1]

#---------------------------------------------
sayilar = [3, 2, 5, 6, -7, 14, 4, -5, -6, -5, -3, 11, 110, -15]

def ciftMi(s):
    return s % 2 == 0

def tekMi(s):
    return s % 2 == 1

ciftSayilar1 = list(filter(lambda s:s%2==0,sayilar))
tekSayilar1 = list(filter(lambda s:s%2==1,sayilar))

ciftSayilar2 = list(filter(ciftMi, sayilar))
tekSayilar2 = list(filter(tekMi, sayilar))

ciftSayilar3 = [sayi for sayi in sayilar if sayi not in tekSayilar2]

#---------------------------------------------
# map()
sayilar = [3, 2, 5, 6, -7, 14, 4, -5, -6, -5, -3, 11, 110, -15]

def kareAl(s):
    return s**2

sayilarinKaresi = []
for sayi in sayilar:
    sayilarinKaresi.append(sayi**2)
print(sayilarinKaresi)

sayilarinKaresi2 = tuple(map(kareAl, sayilar))
sayilarinKaresi3 = tuple(map(lambda s:s*s, sayilar))

print(sayilarinKaresi2)
print(sayilarinKaresi3)

#---------------------------------------------
# reduce()
from functools import reduce
sayilar = [3,4,6,-1,7]

def cikar(s1,s2):
    return s1-s2

toplam1 = reduce(cikar, sayilar)
toplam2 = reduce(lambda s1,s2:s1+s2,sayilar)

#---------------------------------------------
# çarpma işlemi
# en büyük ve en küçük sayıyı bulma
from functools import reduce

sayilar = [2,1,6,5,4,8,-2,-4]

def carp(s1,s2):
    return s1*s2

carpimSonucu = reduce(carp, sayilar)

def enBuyukSayi(s1,s2):
    if s1 > s2:
        return s1
    return s2

enBuyukSayi1 = reduce(enBuyukSayi, sayilar)
enBuyukSayi2 = reduce(lambda s1,s2:s1 if s1 > s2 else s2, sayilar)
print(max(sayilar))

enKucukSayi = reduce(lambda a,b: a if a > b else b, sayilar)
print(min(sayilar))

#---------------------------------------------
# map ve reduce Fonksiyonu - Örnek

katSayilar = [0.2, 0.3, 0.5]
notlar = [60,40,70]

donemSonuNotlar1 = []
for i in range(3):
    donemSonuNotlar1.append(katSayilar[i] * notlar[i])
print(donemSonuNotlar1)

donemSonuNotlar2 = list(map(lambda s1,s2:s1*s2, katSayilar, notlar))
donemSonuNotu = reduce(lambda s1,s2:s1+s2, donemSonuNotlar2)

#%% Zip Fonksiyonu
numaralar = [1,2,3,4,5]
isimler = ["Cavit","Nida","Aliye","Mert","Ahmet"]

ziplenmis = zip(numaralar,isimler)
bilgiler = list(ziplenmis)

yaslar = (15,8,19,32,45)

bilgiler = list(zip(numaralar,isimler,yaslar))
print(bilgiler)

for bilgi in bilgiler:
    print("No: {} Adı: {} Yaşı: {}".format(bilgi[0],bilgi[1],bilgi[2]))
    
for no, ad, yas in bilgiler:
    print("No: {} Adı: {} Yaşı: {}".format(no,ad,yas))

ziplenmis = zip(numaralar, isimler)
print(list(ziplenmis))
ziplenmis = zip(numaralar, isimler)
bilgiler = dict(ziplenmis)
print(bilgiler)

#%% enumerate, all, any
sayilar = (20,30,40,50,111)
count = 1
for sayi in sayilar:
    print("{}. sayı = {}".format(count, sayi))
    count += 1
    
print(list(enumerate(sayilar)))
for no, sayi in enumerate(sayilar,1):
    print("{}. sayı = {}".format(no, sayi))

set1 = {4,2,6,7,1}
print(list(enumerate(set1,1)))

rehber = {'Fatih':103234, 'Selim':5465168}
print(list(enumerate(rehber.values(),1)))

# all() # bütün değerler True return True
# any() # en az 1 tanesi True return True

# Tamamı True mu?
print(all([True,True,True]))
print(all([True,False,True]))

# Herhangi bir tanesi True mu?
print(any([True,True,True]))
print(any([True,False,True]))
print(any([False,False,False]))

#%% Bir Fonksiyonun Fonksiyon Döndürmesi
def bilgiVer3(func):
    print("Bilgi Veriliyor...")
    return func

def kullaniciBilgisiVer(isim):
    return "Adı: " + isim

#print(kullaniciBilgisiVer("Cavit Batu"))
print(bilgiVer3(kullaniciBilgisiVer)("Cavit Batu"))

#%% Decorators (Süslemeler)
def funcInfo(func):
    def bilgiVer4():
        print("Fonksiyonun çalışma başladı!")
        func()
        print("Fonksiyonun çalışma bitti")
    return bilgiVer4

@funcInfo    
def soruSor():
    print("Soru Sordum")
    
def cevapVer():
    print("Cevap Verdim")

#funcInfo(soruSor)()
#funcInfo(cevapVer)()

#---------------------------------------------
# Argüman İletimi 
def funcInfo(func):
    def inner(*args, **kwargs):
        print("Konuşma başladı!")
        func(*args, **kwargs)
        print("Konuşma bitti!")
    return inner

def soruSor1(isim,yas,soru, **kwargs):
    print("Soru soran kişinin bilgileri: ")
    print("Adı: {}, Yaşı: {}".format(isim, yas))
    print("Sorusu: {}".format(soru))
    print(kwargs['bilgi'])
    try:
        print(kwargs['bilgi'])
    except Exception:
        print("Elimizde bir bilgi bulunmamaktadır")

@funcInfo
def cevapVer1(isim, yas, cevap):
    print("Cevap veren kişinin bilgileri: ")
    print("Adı: {}, Yaşı: {}".format(isim, yas))
    print("Sorusu: {}".format(cevap))

#funcInfo(soruSor1)("Cavit",19,"Naber",bilgi = "Soru sormak güzeldir")     
#funcInfo(soruSor1)("Mert",18,"İyi misin?")     
#funcInfo(cevapVer1)("Batu",20,"İyiyim")     
soruSor1("Cavit",19,"Naber",bilgi = "Soru sormak güzeldir")   
soruSor1("Mert",18,"İyi misin?")
cevapVer1("Batu",20,"İyiyim")

#---------------------------------------------
import time
# 12 Ağustos 2025
print(time.time())

def calismaSuresiniHesaplama(func):
    def inner(*args, **kwargs):
        baslangic = time.time()
        func(*args, **kwargs)
        bitis = time.time()
        print("Fonksiyonun çalışma süresi: ", bitis-baslangic, "saniyedir")
    return inner    
    
@calismaSuresiniHesaplama
def karekokAl(sayilar):
    sayilar = [sqrt(sayi) for sayi in sayilar]
    return sayilar

@calismaSuresiniHesaplama
def kareAl(sayilar):
    sayilar = [sayi**2 for sayi in sayilar]
    return sayilar

sayilar = list(range(10000))
#print(calismaSuresiniHesaplama(karekokAl)(sayilar))
#print(calismaSuresiniHesaplama(kareAl)(sayilar))
karekokAl(sayilar)
kareAl(sayilar)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    