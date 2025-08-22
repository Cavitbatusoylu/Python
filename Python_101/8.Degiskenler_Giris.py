# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 09:59:27 2025

@author: cavit
"""

sayi1 = 155
sayi2 = 155
print(sayi1*2)
print(sayi2*5)

print("1deneme".isidentifier()) #False
print("deneme1".isidentifier()) #True
print("print".isidentifier()) #True

#%% int

sayi1 = 122
sayi2 = 49

print("Toplama:", sayi1+sayi2)
print("Çıkarma:", sayi1-sayi2)
print("Çarpma:", sayi1*sayi2)
print("Bölme:", sayi1/sayi2)

print(type(sayi1))
print(type(sayi2))

print(id(sayi1))
sayi3 = 122
print(id(sayi3))
sayi3 = 144
print(id(sayi3))

#%% float

sayi1 = 15.4
sayi2 = 16.3

print("Toplama:", sayi1+sayi2)
print("Çıkarma:", sayi1-sayi2)
print("Çarpma:", sayi1*sayi2)
print("Bölme:", sayi1/sayi2)

print(sayi1,type(sayi1))
print(sayi2,type(sayi2))

sayi3 = 15.0
sayi4 = 15

print(sayi3,type(sayi3))
print(sayi4,type(sayi4))

#%% string

isim = "Cavit Batu"
soyad = 'Soylu'

print(isim,type(isim))
print(soyad,type(soyad))

# length
print(len(isim))
print(len(soyad))

print(isim,soyad)

# concetenate
isminTamami = isim + " " + soyad

print(isminTamami)

print(isminTamami[0],isminTamami[6],isminTamami[11], sep = ".")

#%% string Elemanlarına Ulaşma

#Immutable(Değiştirilemez)
kelime = "Fener"
print(kelime)
print(kelime[0])
#kelime[0] = 'S'
#kelime = Salata

kelime = "S" + kelime[1:]
print(kelime)

takim = "Fenerbahce"

kelime1 = takim[6:]
kelime2 = takim[6:]
print(kelime2)
kelime2 = "S" + kelime2[1:]
print(kelime1)
print(kelime2)
kelime3 = takim[3:6]
print(kelime3)

yer = "Istanbul" 
# start, stop, step
print(yer[0::2])
print(yer[0::3])

isim = "batu"
print(isim[::-1])

isim = "diyarbakır"
print(isim[7:4:-1])

#%% Objelerin RAM'de depolanması

# heap
import sys
sayi = 1
str1 = "Python EğitimiiiğÇÖŞİf"
print(sys.getsizeof(sayi))
print(sys.getsizeof(str1))

meyve = "Erik"
print(meyve[0])
print(meyve[1])
print(meyve[2])
print(meyve[3])

#%% Type Conversion(Tip Dönüşümü)

x = 6
y = 5.8
z = "185"

print(int(y))
print(float(x))

print(z*2)
print(int(z)*2)

z = "a185"
#print(int(z))
#print(float(z))
z = "8.7"
print(float(z))
#print(int(z))
print(int(float(z)))

z = "192"

print(float(z))

print(17//6)
print(17/6)
print(int(17/6))

#int -> float
print(float(7))

#string -> float
print("167.8"*2)
print(float("167.8")*2)

#%% Kullanıcıdan Girdi Alma

girdi1 = input("Lütfen bir kelime giriniz: ")
print("Girdiğiniz kelime: ",girdi1)

#%% 

sayi1 = int(input("Lütfen 1.tam sayıyı giriniz:"))
sayi2 = int(input("Lütfen 2.tam sayıyı giriniz:"))
# sayi1 = int(sayi1)

print("{} sayısının 5 katı = ".format(sayi1),5*sayi1)
print("{} sayısının 5 katı = ".format(sayi2),5*sayi2)
print("{} + {} = {}".format(sayi1,sayi2,sayi1+sayi2))

#%%

isim = input("İsminizi giriniz: ")
dogumYili = int(input("Doğum Yılınızı giriniz = "))

print("Merhabalar {}, {} yaşındasınız!".format(isim,2025-dogumYili))
