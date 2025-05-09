meyveler = ["elma", "armut", "muz"]

print(meyveler[2])

meyveler.append("çilek")

meyveler.insert(1, "kiraz")

meyveler.remove("armut")

print(meyveler)

meyveler.sort()
print(len(meyveler))


koordinat = (10, 20)

print(koordinat[0])

koordinat[0] = 50 # hata verir çünkü tuple değiştirilemez


sayilar = {1, 2, 3, 4, 4, 5}
demo = {1, 2, 3, 4, 5}

print(sayilar) # küme içinde tekrar eden elemanlar yok sayılır

print(sayilar[0]) # hata verir çünkü küme sıralı değildir

sayilar.add(6) # küme eleman ekleme
sayilar.remove(2) # küme eleman silme
print(sayilar)

a = {1, 2, 3}
b = {3, 4, 5}
print(a - b)

ogrenci = {
    "ad": "Cavit",
    "yas": 20,
    "sehir": "Manisa"
}

print

ogrenci["yas"] = 22

ogrenci["okul"] = "YTÜ" # hata verir çünkü okul anahtarı yok

print(ogrenci.keys()) # anahtarları alır
print(ogrenci.values()) # değerleri alır