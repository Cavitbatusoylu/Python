# KONU OOP Object Oriented Programming (Nesneye Yönelik Programlama)

# Object Oriented Programming
    # Her şey bir objedir. Hayatta görünen her şey bir objedir.
    # Her objenin Attribute'leri vardır. (Attribute, property, özellikler)(isim, yaş, göz rengi vs.)
    # Her objenin Behaviour'ları vardır. (Metotlar) (yürümek, konuşmak vs.)
# Functional Programming
# Procedure Oriented Programming

# Class - Design (blueprint) (Taslak)
# Object - Instance (Örnek)

# Inheritance (Kalıtım)
# Encapsulation (Kapsülleme)
# Abstraction (Soyutlama)
# Polymorphism (Çok çeşitlilik)

# Televizyon
    # Üretim Yeri
    # Marka
    # Model
    # Ekran boyutu
    # Şekil
    # Görüntü kalitesi
    # Diğer özellikleri

    # Aç/Kapa
    # Kanal görüntüleme
    
#%% 
a = 5 
a = int(5)
print(type(a))

b = 5.5
b = float(6.7)
print(type(b))

c = "naber"
print(type(c))

print(c)
print(c.capitalize())
print(c)
c = c.capitalize()
print(c)

liste = [4,3,7]
print(liste)
print(type(liste))
liste.sort(reverse = True)
print(liste)

print(type((4,5,6)))
print(type({8,4,9}))
print(type(None))
print(type(True))
print(type({1:'Python'}))

#%% Kendi class'ımızı (sınıfımı - veri tipimizi oluşturma)
class Insan:
    # Attributes (Özellikleri)(Variables - Değişkenleri)
    # Behaviours (Davranışlar)(Methods - Metotlar)(Fonksiyonlar)
    
    # ad, soyad, yas, meslek
    
    # constructor - yapıcı metot
    def __init__(self, ad, soyad, yas, meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.meslek = meslek
    def bilgiSoyle(self):
        print("İnsanın bilgileri:")
        print("Adı Soyadı: {} {}".format(self.ad,self.soyad))
        print("Yaşı : {}".format(self.yas))
        print("Mesleği: {}".format(self.meslek))

liste = list()

#i1 objesi Insan sınıfının bir instance'ı
i1 = Insan("Cavit","Soylu", 20, "Bilgisayar Mühendisi") # instantiate - oluşturma

#i1.ad = "Cavit"
#i1.soyad = "Soylu"
#i1.yas = 20
#i1.meslek = "Bilgisayar Mühendisi"

i2 = Insan("Kazım", "Karaca", 18, "Yapay Zeka Mühendisi")

#i2.ad = "Kazım"
#i2.soyad = "Karaca"
#i2.yas = 18
#i2.meslek = "Yapay Zeka Mühendisi"

#print(i1.ad, i1.soyad, i1.yas, i1.meslek)
#print(i2.ad, i2.soyad, i2.yas, i2.meslek)

i1.bilgiSoyle()
i2.bilgiSoyle()

Insan.bilgiSoyle(i1)
Insan.bilgiSoyle(i2)

#%%
class Araba:
    
    def __init__(self,marka,model,yil,bakim = True):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.bakim = bakim
        
    def ozellikleriGoster(self):
        print(self.marka, self.model, self.yil, end = " ")
        self.bakimDurumunuGoster()

    def bakimDurumunuGoster(self):
        if self.bakim:
            print("Bakımı Yapılmış.")
        else:
            print("Bakımı Yapılammış")
            
a1 = Araba("BMW","5.20",2022)
a2 = Araba("Ferrari","P80/C",2015,False)

a1.ozellikleriGoster()
a2.ozellikleriGoster()

a3 = Araba(yil = "2017", bakim = False, marka = "Toyota", model = "Corona")
a3.ozellikleriGoster()

#%% Variable Çeşitleri
# 1-) Instance Variable
# 2-) Class/Static Variable

class User:
    # Class namespace
    sayac = 0
    def __init__(self, isim = "isim yok", kayitTarihi = "20.12.2012"):
       # Object/Instance namespace
         User.sayac += 1
         self.isim = isim
         self.kayitTarihi = kayitTarihi


print(User.sayac)
user1 = User("Mehmet Baki","01.05.2020")
print(User.sayac)
print(user1.sayac)

user2 = User("Elmas Maden","06.09.2021")
print(User.sayac)
print(user2.sayac)

del user2
User.sayac -= 1
print("Kullanıcı Silindi!")

print(User.sayac)

#%% Metot Çeşitleri
# 1-) Instance (Obje) Methods
# 2-) Class Methods
# 3-) Static (Obje) Methods

class Calisan:
    sirket = "Türk Telekom"
    def __init__(self, isim, soyad, sabitMaas, prim):
        self.isim = isim
        self.soyad = soyad
        self.sabitMaas = sabitMaas
        self.prim = prim
        
    # Obje Metotu
    def toplamMaas(self):
        return self.sabitMaas + self.prim
    
    # Sınıf Metotu
    @classmethod
    def sirketIsminiSoyle(cls):
        return cls.sirket
    
    @staticmethod
    def bilgi(info = None):
        if info != None:
            print(info)
        else:
            print("Yazdırılacak bilgi bulunamadı!")

c1 = Calisan("Aysel","Gündoğan",5500, 1750)
c2 = Calisan("Mehmet","Kasap",7500, 1250)

print(c1.toplamMaas())
print(c2.toplamMaas())

print(Calisan.toplamMaas(c1))
print(Calisan.toplamMaas(c2))

print(Calisan.sirketIsminiSoyle())
print(c1.sirketIsminiSoyle())
print(c2.sirketIsminiSoyle())

Calisan.bilgi("Doğrudan bilgiyi yaz!")
Calisan.bilgi()

#%% Inner Sınıflar

#outer class
class Musteri:
    def __init__(self, musteriNo, isim, soyad, bakiye, hesapTuru):
        self.musteriNo = musteriNo
        self.isim = isim
        self.soyad = soyad
        self.bakiye = bakiye
        self.hesapTuru = hesapTuru
        
    def bilgileriGoster(self):
        print(self.musteriNo, self.isim, self.soyad)
        
    #Inner Class   
    class Hesap:
        def __init__(self, bakiye, hesapTuru):
            self.bakiye = bakiye
            self.hesapTuru = hesapTuru
        def bilgileriGoster(self):
            print(self.bakiye, self.hesapTuru)
        
            
m1 = Musteri(1, "Selim", "Kapı", 5000, "TL")
m2 = Musteri(2, "Emel", "Toprak", 4500, "Dolar")

m1.bilgileriGoster()
m2.bilgileriGoster()

hesap = Musteri.Hesap(6000, "Euro")
hesap.bilgileriGoster()

m1.hesap = hesap
m1.bilgileriGoster()
















