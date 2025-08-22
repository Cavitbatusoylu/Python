sayi1 = 5
sayi2 = 5.5

print(isinstance(sayi1, int))
print(isinstance(sayi2, float))

help(list)

print(issubclass(list, object))
print(issubclass(int, object))

class A:
    pass
class B(A):
    pass
class C(B):
    pass

print(issubclass(A, B)) # False
print(issubclass(B, C)) # False
print(issubclass(C, A)) # True
print(issubclass(B, A)) # True

#%% 
class A:
    def metot1(self):
        print("A metot 1")
    def metot2(self):
        print("A metot 2")
        
class B(A):
    def metot3(self):
        print("B metot 3")
    def metot4(self):
        print("B metot 4")
        
class C(B):
    def metot5(self):
        print("C metot 5")
        
aObjesi = A()
bObjesi = B()
cObjesi = C()

aObjesi.metot1()
aObjesi.metot2()

bObjesi.metot1()
bObjesi.metot2()
bObjesi.metot3()
bObjesi.metot4()

cObjesi.metot1()
cObjesi.metot2()
cObjesi.metot3()
cObjesi.metot4()
cObjesi.metot5()

# method resolution order
# metot çözümleme sıralaması
C.mro()

# A super class (parent class)
# B sub class (child class)

# B->A single level inheritance
# C->B->A multi level inheritance
# C->(A,B) multiple level inheritance

#%% 
class X:
    def metot1(self):
        print("X metot 1")

class Z:
    def metot1(self):
        print("Z metot 1")

class Y:
    def metot1(self):
        print("Y metot 1")

class A(X,Y):
    def metot1(self):
        print("A metot 1")

class B(Y,Z):
    def metot1(self):
        print("B metot 1")

class C(B,A,Z):
    def metot1(self):
        print("C metot 1")

c1 = C()
c1.metot1()

print(C.mro())

#%%
class D:
    def __init__(self):
        print("D constructor")
    def metot1(self):
        print("D metot 1")

class E:
    def __init__(self):
        print("E constructor")
    def metot1(self):
        print("E metot 1")
        
class F(D,E):    
    def __init__(self):
        print("F constructor")
        super().__init__()
        D.__init__(self)
        E.__init__(self)
    def metot1(self):
        print("F metot 1")
        super().metot1()

fObj = F()
#fObj.metot1()
print(F.mro())

#%% Finans haberleri  olmak üzere ikiye ayrılmaktadır. Her haberin başlığı, içeriği ve bir adet görseli bulunmaktadır.
# Spor haberlerinde video içerikleri de bulunmaktadır. Finans haberlerinde döviz kurlarının bilgileri de yer almaktadır.
# Modelleyiniz.

class Genel:
    def __init__(self, baslik, icerik, gorsel):
        self.baslik = baslik
        self.icerik = icerik
        self.gorsel = gorsel
    def bilgileriGoster(self):
        print(self.baslik, self.icerik, self.gorsel)

class Spor(Genel):
    def __init__(self, baslik, icerik, gorsel, video):
        super().__init__(baslik, icerik, gorsel)
        self.video = video
    def bilgileriGoster(self):
        super().bilgileriGoster()
        print("Video:", self.video)
    def videoOynat(self):
        print(self.video, "isimli video oynatılıyor...")

class Finans(Genel):
    def __init__(self, baslik, icerik, gorsel, dovizKurlari):
        super().__init__(baslik, icerik, gorsel)
        self.dovizKurlari = dovizKurlari

    # Döviz bilgilerini göster
    def dovizKurlariBilgisiniGoster(self):
        for dovizAdi, dovizDegeri in self.dovizKurlari.items():
            print(dovizAdi, ":", dovizDegeri)

    # Döviz bilgilerini güncelle
    def dovizKurlariGuncelle(self, yeniKurlar):
        self.dovizKurlari.update(yeniKurlar)
        print("Döviz kurları güncellendi!")

# Örnek kullanım
s1 = Spor(video="video1.mp4", baslik="Macta kazanan olmadı!", icerik="0-0 bitti!", gorsel="foto1.png")
f1 = Finans(dovizKurlari={'Dolar':40, 'Euro':47, 'Sterlin':55}, baslik="Ekonomi tüm dünyada durgun!", icerik="Küresel salgın tüm dünyayı etkiledi", gorsel="foto2.png")

# Spor haberini göster
s1.bilgileriGoster()
s1.videoOynat()

# Finans haberini göster
f1.bilgileriGoster()
f1.dovizKurlariBilgisiniGoster()

# Döviz kurlarını güncelle
guncelKurBilgisi = {"Dolar": 40.2, "Euro": 47.8, "Sterlin": 55.4}
f1.dovizKurlariGuncelle(guncelKurBilgisi)
f1.dovizKurlariBilgisiniGoster()
















