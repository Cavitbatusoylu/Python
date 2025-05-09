def selamla():
    print("Merhaba Dünya")

selamla()

def selamla(isim):
    print("Merhaba {isim}")

selamla("Cavit")

def topla(x, y):
    return x + y

sonuc = topla(5,6)
print(sonuc)

def topla(*sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

print(topla(1,2,3,4,5))

def bilgiler(**kişi):
    for anahtar, deger in kişi.items():
        print(f"{anahtar}: {deger}")

bilgiler(ad="Cavit", yas=19, sehir="Manisa")

kare = lambda x: x * x
print(kare(5))

def kullanici_topla():
    a = input("Birinci sayıyı girin: ")
    b = input("İkinci sayıyı girin: ")
    print("Toplam:", a + b)

kullanici_topla()