# -*- coding: utf-8 -*-


# =======================================
# NoneType (None Tipi)
# Numeric (Sayısal) Tiplere Giriş
# int, float
# bool
# complex (kompleks sayılar)

# Dizi Halindeki Veri Tiplerine Giriş
# List (Liste) Veri Tipi
# Tuple Veri Tipi
# Set Veri Tipi
# String (Karakter Dizisi) Veri Tipi
# Range (Aralık)
# Dictionary (Sözlük)
# =======================================

#%% NoneType(None Tipi)

sehir = None
print(type(sehir))

sehir = "İstanbul"
print(type(sehir))

#%% Numeric (Sayısal) Tiplere Giriş

# int, float
x = 10
y = int(15)

z= 10.7
t = float(17.8)

x1 = float(x)
z1 =int(z)
t1 = int(t)

# bool
anahtar1 = True
anahtar2 = False

k1 = 3 < 4

anahtar3 = bool(True)
anahtar4 = bool(False)

anahtar5 = bool(10)
anahtar6 = bool(1.2)
anahtar7 = bool(-6)

anahtar8 = bool(0.0)
anahtar9 = bool(0)

anahtar10 = int(True)  # 1
anahtar11 = int(False) # 0

anahtar12 = float(True) #1.0
anahtar13 = float(False) #0.0

# complex (kompleks sayılar)
ks1 = 2 + 3j
ks2 = complex(4,5) # 4 + 5j

toplam = ks1 + ks2
cikar = ks1 - ks2
carp = ks1 * ks2 #(2+3j)(4+5j) = 8 + 10j + 12j + (-15) = -7 + 22j
bol = ks1/ks2

sayi1 = 4.5
sayi2 = 7

ks3 = complex(sayi1,sayi2)
ks4 = sayi1 + sayi2*1j

#%% Dizi Halindeki Veri Tiplerine Giriş

# List (Liste) Veri Tipi
## Mutable (Değiştirilebilir)
## Elemanlarının sequence number(sıra numarası) vardır.
## list()    []
liste1 = list([1,5,7,8,3])
liste2 = [6,4,9,7,8,10,-5]

print(liste1)
liste1[3] = 100
print(liste1)

print(liste2)
liste2[2] = 1000
print(liste2)

# Tuple Veri Tipi
## Immutable (Değiştirilemez)
## Read-Only (Sadece Okunabilir)
## Elemanların sequence number (sıra numarası) vardır.
liste1 = [2,4,7,10]
tuple1 = (7,8,11,-5)

tuple2 = tuple("Cavit")
tuple3 = tuple([2,1,8,9,10])
tuple4 = tuple((6,1,8,9,11,16,-5,0,2))
tuple5 = tuple(["C","A","V","İ","T"])
tuple6 = tuple(["C","A","V","İ","T"])

x = 5
y = int(10)

print(liste1, tuple1)
liste1[0] = 14
print(liste1, tuple1)

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])


# Set Veri Tipi

# String (Karakter Dizisi) Veri Tipi
## Immutable (Değiştirilemez)
## Elemanların sequence number (sıra numarası) var
karakter1 = "C"
karakter2 = "C"

isim = "Cavit Batu"
print(isim)

isim = isim[:6] + "Soylu"
print(isim)

print(isim[0])
print(isim[1])

isim = "T" + isim[1:]
print(isim)


# Range (Aralık)
aralik = range(10) # [0,10) x € Z
print(aralik, type(aralik))

print(*aralik)
print(*aralik)

listAralik = list(aralik)
tupleAralik = tuple(aralik)
setAralik = set(aralik)

print(list(aralik))
print(tuple(aralik))
print(set(aralik))

print(str(aralik))
print(str("range(0, 10)"))
print(str(aralik)[0:5])
print(str(listAralik))
print(str(listAralik)[0])
print(str(listAralik)[1])
print(str(listAralik)[2])
print(str(listAralik)[3])

#range(start=0,stop,step=1)
aralik1 = range(18,2,-5)
print(list(aralik1))

aralik1 = range(5,14)
print(list(aralik1))


# Dictionary (Sözlük)
# Mutable (Değiştirilebilir)
# Elemanların sequence number(sıra numarası) yerine "KEY" vardır
# dict()   {}
set1 = {"Cavit","İlayda","Aliye"}
sozluk = {1:"Cavit",2:"İlayda",5:"Aliye"}

print(sozluk[5])
print(sozluk.get(2))
#print(sozluk[3])
print(sozluk.get(3,"Bu anahtar sözlükte bulunmamaktadır"))

bosSozluk1 = {}
bosSozluk2 = dict()
anahtarlar[1,2,3]
sozluk2Elemanlari = zip(anahtarlar,degerler)
print(*sozluk2Elemanlari)
sozluk2Elemanlari = zip(anahtarlar,degerler)
sozluk1 = dict(sozluk2Elemanlari)
sozluk2 = dict([(1,"A"),(2,"B"),(3,"C")])
print(sozluk1)
print(sozluk2)


#%% Tuple (Demet) Veri Tipi

## Tuple Giriş ve Tuple Oluşturma
### tuple() ()
tup1 = (15,26,17,25)
tup2 = ("Ahmet","Mehmet")
tup3 = (5+4j, "Melih",74.8,159)
tup4 = tuple([79,125,1748,14.69])
#tup1[0] = 174
butunTupler = tup1 + tup2 + tup3 + tup4


# Tuple Elemanlarına Erişmek
tup1 = (15,26,17,25,178)
liste1 = [1,7,9,3,8]
print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])

print(tup1[1:])
print(liste1[2:4])

print(tup1[::2])
print(tup1[0:len(tup1):2])
print(tup1[-1::-1])
print(tup1[-1:0:-1])


# Tuple Metotları
tup = (15,26,17,25,178,26,17,26,51)
print(tup.count(26))
print(tup.index(26))
print(tup.index(178))

#%% List (Liste) Veri Tipi

## Liste Elemanlarına Erişmek
liste1 = [6,4,9,7,8,10,-5]
print(liste1[0])
print(liste1[1])
print(liste1[6])

print(liste1[2:5]) # liste1[2] liste1[3] liste1[4]
print(liste1[1:6:2])

print(liste1[6])
# len = length = uzunluk
print(liste1[len(liste1)-1])
print(liste1[-1])
print(liste1[0])
print(liste1[-7])
print(liste1[-len(liste1)])

print(liste1)
print(liste1[:])
print(liste1[::])
print(liste1[::2])


## Listelerde Ekleme, Güncelleme ve Silme
isimler = ['Cavit','Batu','Gül','Manolya']
yaslar = [28,35,44,48]

print(isimler)
isimler = isimler + ["Mert","Mehmet"]
print(isimler)

print(isimler)
isimler[0] = "Yavuz"
print(isimler)

print(isimler[1:4])

print(isimler)
isimler[1:4] = ["Selim","Oya","Melike"]
print(isimler)
isimler[1:4] = "Selim","Oya","Melike"
print(isimler)

#delete - silmek
del isimler[5]
print(isimler)

isimler = isimler[:1] + isimler[3:]
print(isimler)


## Liste Metotları
isimler = ['Cavit','Batu','Gül','Manolya']
yaslar = [28,35,44,48]

karisikListe = isimler + yaslar
karisikListe.extend({14.7,"Selma",None,True,5+7j})
karisikListe += [True,False,9+7j,"Naber?"]
print(karisikListe.index(9+7j))
karisikListe.append(175)
karisikListe.insert(2,159874)
karisikListe.pop()
karisikListe.pop(7)

karisikListe.extend([100,100,100])
karisikListe.remove(100)
karisikListe[0] = 100
karisikListe.remove(100)

liste = [2,5,7]
print(liste)
liste.reverse()
print(liste)

liste += [-5,8,4,3,10,-9]
liste.sort()
print(liste)

print(isimler)
isimler.sort()
print(isimler)

## Çok Boyutlu Listeler
isimler = ["Cavit","Batu","Mert","Nehir"]
yaslar = [37,47,55,32]
bilgiler = [["Cavit",37],["Batu",47],["Mert",55],["Nehir",32]]

print(bilgiler[0])
print(bilgiler[1])
print(bilgiler[2])
print(bilgiler[3])

print(bilgiler[0][0])
print(bilgiler[0][1])

bilgiler = [({187:"Cavit"},{180:"Mert"}),("Van","Ardahan")]

print(bilgiler[0])
print(bilgiler[0][0][187])
print(bilgiler[0][1][180])
print(bilgiler[1][0])
print(bilgiler[1][1])

#%% Set (Benzersiz) Veri Tipi

# Mutable (Değiştirilebilir)
# Elemanların Sequence Number (Sıra Numarası) yoktur
# İçerisinde aynı değerde elemanlar barındırmaz
# {}

set1 = {5,12,2,6,5,12,2}
print(set1)

set1.remove(12)
print(set1)

set2 = set([5,4,7,8,9,4,7,-5,0,100])
print(set2)


## Setlerde Eleman Ekleme ve Silme
set1  ={4,1,8,9,-5,0,91}
print(set1)

set1.add(150)
print(set1)

set1.clear()
print(set1)

set1.update({4,1,8,9,-5,0,-91})
print(set1)

print(set1.pop())
print(set1)

set1.remove(-5)
print(set1)
#set1.remove(180)


## Set Metotları
set1 = {4,1,8,9,-5,0,91,"Kazım","Cavit"}
set2 = {3,4,8,7,-6,14,51,66,78,"Batu","Mert"}
set3 = {3,4,8}
set4 = {100,200,300}

set5 = set1.copy()
print(set1)
print(set5)
set1.remove(8)
print(set1)
print(set5)

print(set1.difference(set2))
set1 = set1.difference(set2)
set1.difference_update(set2)
print(set1)

set1 = {4,1,8,9,-5,0,91,"Kazım","Cavit"}
set2 = {3,4,8,7,-6,14,51,66,78,"Batu","Mert"}
set3 = {3,4,8}
set4 = {100,200,300}

set1.discard(150)
set1.discard(91)
print(set1)

print(set1.intersection(set2))
print(set1)
set1.intersection_update(set2)
print(set1)

set1 = {4,1,8,9,-5,0,91,"Kazım","Cavit"}
set2 = {3,4,8,7,-6,14,51,66,78,"Batu","Mert"}
set3 = {3,4,8}
set4 = {100,200,300}

print(set3.isdisjoint(set4))
print(set1.isdisjoint(set2))

print(set3.issubset(set2))
print(set2.issubset(set3))

print(set1)
set1.pop()
print(set1)

set1 = {4,1,8,9,-5,0,91,"Kazım","Cavit"}
set2 = {3,4,8,7,-6,14,51,66,78,"Batu","Mert"}
set3 = {3,4,8}
set4 = {100,200,300}

print(set1.symmetric_difference(set2))
print(set1)
set1.symmetric_difference_update(set2)
print(set1)

set1 = {4,1,8,9,-5,0,91,"Kazım","Cavit"}
set2 = {3,4,8,7,-6,14,51,66,78,"Batu","Mert"}
set3 = {3,4,8}
set4 = {100,200,300}

print(set1.intersection(set2)) # Ortak elemanları bulur
print(set1.symmetric_difference(set2)) # Sadece birinde bulunan elemanları verir.
print(set1.union(set2)) #Tüm elemanları döndürür.

#%% Sözlüklerde Seçme, Ekleme, Güncelleme ve Silme
keys = ("Cavit","Mert","Sema")
values = ['Bilgisayar Mühendisi',
          'Elektrik Elektronik Mühendisi',
          "Avukat"]

sozlukElemanlari = zip(keys, values)
#print(*sozlukElemanlari)

bilgiler = dict(sozlukElemanlari)
print(bilgiler)

print(bilgiler["Kaan"])
print(bilgiler["Aliye"])

# Sözlükte anahtar değeri yoksa o zaman ekler
bilgiler["Kerem"] = "Uçak Mühendisi"
print(bilgiler)

# Güncelleme
bilgiler["Zeynep"] = "Doktor"
print(bilgiler)

# Silme
del bilgiler["Sema"]
print(bilgiler)


# Sözlük Metotları
ogrencilerDers = {'Okan':'Makine Mühendisi',
                  'Armağan': ('Bilgisayar Ağları',
                              'Doğal Dil İşleme'),
                  'Cavit':('Makine Öğrenmesi',
                           'Doğal Dil İşleme'),
                  'Batu':[{'Ders Adı':'Veri Tabanı','Hoca':'Ömer'},
                          {'Ders Adı': 'Doğal Dil İşleme': 'Hoca':' Burak'}]}

print(ogrencilerDers['Okan'])
print(ogrencilerDers['Batu'])
print(ogrencilerDers['Batu'][0])
print(ogrencilerDers['Batu'][1])
print(ogrencilerDers['Batu'][0]['Ders Adı'])
print(ogrencilerDers['Batu'][1]['Ders Adı'])

baskaSozluk = ogrencilerDers.copy()
baskaSozluk['Okan'] = "Matematik 1"
sozluk1 = dict(.fromkeys(['Ali','Ahmet','Aslı'],0))
print(sozluk1)
print(ogrencilerDers.get('Okan'))
print(sozluk1.get('Okan',' Bu anahtara sahşp bir değer bulunamadı'))
print(ogrencilerDers.items())
print(ogrencilerDers.keys())
print(ogrencilerDers.values())

print(30*'-')
print(ogrencilerDers)
ogrencilerDers.pop("Armağan")
print(30*'-')
print(ogrencilerDers)
print(30*'-')
ogrencilerDers.popitem()
print(ogrencilerDers)
print(30*'-')
ogrencilerDers.popitem()
print(ogrencilerDers)
print(30*'-')
ogrencilerDers.popitem()
print(ogrencilerDers)

ogrencilerDers = {'Okan':'Makine Mühendisi',
                  'Armağan': ('Bilgisayar Ağları',
                              'Doğal Dil İşleme'),
                  'Cavit':('Makine Öğrenmesi',
                           'Doğal Dil İşleme'),
                  'Batu':[{'Ders Adı':'Veri Tabanı','Hoca':'Ömer'},
                          {'Ders Adı': 'Doğal Dil İşleme': 'Hoca':' Burak'}]}

ogrencilerDers.setdefault('Okan','DERS ALMADI')
ogrencilerDers.setdefault('Mehmet','DERS ALMADI')
print(ogrencilerDers)

sozluk2 = {'Cavit':'Bilgisayar 1'}
ogrencilerDers.update(sozluk2)

sozluk3 = {'Nida':'Yüksek Matematik 1'}
ogrencilerDers.update(sozluk3)
print(ogrencilerDers)









































 


