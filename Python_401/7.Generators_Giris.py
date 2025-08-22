# -*- coding: utf-8 -*-

# KONU - Generators (Üreteçler)
# Her generator bir iteratördür.
# yield => verim, ürün

def sayiUret():
    yield 1
    yield True
    yield "Cavit Batu Soylu"
    
uretilmisDegerler = list(sayiUret())

for sayi in uretilmisDegerler:
    print(sayi)

aralik = range(10)
print(list(aralik))

print(type(sayiUret))
print(sayiUret)

def ilkBinSayi():
    # yield 0
    # yield 1
    
    # yield 1000
    i = 0
    while i <= 1000:
        yield i
        i += 1
        
print(list(ilkBinSayi()))

sayilar = ilkBinSayi()

print(next(sayilar))
print(next(sayilar))
print(next(sayilar))
print(next(sayilar))
print(next(sayilar))
print(next(sayilar))
print(next(sayilar))

print("next 7 defa çalıştı")

for sayi in sayilar:
    print(sayi)
    
#%% 
def katiniUret(sayilar, kati):
    for sayi in sayilar:
        yield sayi * kati

sayilar = [7,15,21,14]

sayilarin3Kati1 = katiniUret(sayilar, 3)
print(list(sayilarin3Kati1))

sayilarin3Kati2 = [sayi * 3 for sayi in sayilar]
print(sayilarin3Kati2)

sayilarinKaresi = [s * s for s in sayilar]
print(sayilarinKaresi)