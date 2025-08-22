# -*- coding: utf-8 -*-

class Arac:
    def __init__ (self, tur):
        self.tur = tur
        
class Araba(Arac):
    def __init__(self):
        super().__init__("Araba")
    def calis(self):
        print("Motor çalıştı")
        print("Hareket etmeye başlayabilirsin")
        
class Motorsiklet(Arac):
    def __init__(self):
        super().__init__("Motorsiklet")
    def calis(self):
        print("Motor çalıştı")
        print("Motor ısınmaya başladı")
        print("Motorun ısınma süreci bitti")
        print("Hareket etmeye başlayabilirsin")

a1 = Araba()
m1 = Motorsiklet()

a1.calis()
m1.calis()

class Insan:
    def git(self, arac: Arac):
        arac.calis()
        print("Hareket etmeye başladığım aracın türü: Araba")
i1 = Insan()
print(20*"*")
i1.git(a1)
print(20*"*")
i1.git(m1)

#%% Operator Overloading

toplam = 6 + 9
fullName = "Cavit" + " " + "Soylu"

sonuc = int.__add__(30,50)
sonuc = 30 + 50

takimIsmi = str.__add__("Fener", "bahçe")
takimIsmi = "Fener" + "bahçe"

#%% Magic Methods (Büyülü Metotlar)

# addition (toplama işlemi) + operatörü
print(int.__add__(7, 8))
print(float.__add__(5.0, 10.0))

# substraction (çıkarma işlemi) - operatörü
print(int.__sub__(10,2))

# multiplicatiion (çarpma işlemi) * operatörü
print(int.__mul__(8,9))
print(int.__mul__(13.2, 11.4))

# division (bölme işlemi) / operatörü
print(int.__truediv__(16, 9))
print(int.__floordiv__(16, 9))
print(int.__divmod__(10, 3))
print(int.__divmod__(17, 4)) # 17 = 4 x 4 + 1

print(str.__mul__('-', 30))
print(30*'-')

print([2,3,4,5,6].__len__()) # length
print(len([2,3,4,5,6,7]))

# greater than > operatörü
print(int.__gt__(5, 4))
print(5 > 4)
print(int.__gt__(4, 5))
print(4 > 5)


# greater or equal >= operatörü
print(int.__ge__(5, 5))
print(int.__ge__(5, 4))
print(int.__ge__(4, 5))

# lower than < operatörü
print(int.__lt__(5, 6))
print(int.__lt__(5, 4))

# lower or equal <= operatörü
print(float.__le__(10.2, 10.2))
print(float.__le__(10.2, 10.3))
print(float.__le__(10.1, 10.2))
print(10.2 <= 10.2)
print(10.2 <= 10.3)
print(10.1 <= 10.2)

#%% 
from math import sqrt
class Nokta:
    sayac = 0
    
    def __init__(self, x, y):
        Nokta.sayac += 1
        self.x = x
        self.y = y

    # + operatörü
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Nokta(x,y)
        
    def __str__(self):
        return f'({self.x},{self.y})'
        
    # > operatörü
    def __gt__(self,other):
        u1 = sqrt(self.x*self.x + self.y*self.y)
        u2 = sqrt(other.x*other.x + other.y*other.y)
        return u1 > u2
    
    # < operatörü
    def __lt__(self,other):
        u1 = sqrt(self.x*self.x + self.y*self.y)
        u2 = sqrt(other.x*other.x + other.y*other.y)
        return u1 < u2
    
    def __del__(self):
        Nokta.sayac -= 1
        print(f'{self} noktası kaldırıldı!')
        
    def __len__(self):
        """
        1. bölgedeyse 1
        2. bölgedeyse 2
        3. bölgedeyse 3
        4. bölgedeyse 4
        Nokta orijindeyse 5
        y ekseni üzerindeyse 6
        x ekseni üzerindeyse 7
        """
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        elif self.x == 0 and self.y == 0:
            return 5
        elif self.x == 0:
            return 6
        elif self.y == 0:
            return 7
n1 = Nokta(5,6)
n2 = Nokta(0,10)
n3 = n1 + n2

print(Nokta.sayac)
print(n3)             # (12,15)
print(str(n3))        # (12,15)

print(n1 > n2)
print(n2 > n1)

print(n1 < n2)
print(n2 < n1)

print(Nokta.sayac)
del n1
print(Nokta.sayac)

if len(n2) in [1,2,3,4]:
    print(f"{n2} {len(n2)}. bölgededir!", format(len(n2)))
elif len(n2) == 5:
    print(f"{n2} Orijindedir!")
elif len(n2) == 6:
    print(f"{n2} y ekseni üzerindedir!")
elif len(n2) == 7:
    print(f"{n2} x ekseni üzerindedir!")

#%% Method overloading, method overriding
def topla(s1,s2):
    return s1+s2

def topla (s1,s2,s3 = 0):
    return s1+s2+s3

print(topla(2,5))
print(topla(2,5,9))

class Bina:
    def __init__(self, no):
        self.binaNo = no
    def adresSoyle(self):
        print("No:",self.binaNo)

class Daire(Bina):
    def __init__(self, no, binaNo):
        self.daireNo = no
        super().__init__(binaNo)
    #method overriding
    def adresSoyle(self):
        print(f"Bina No: {self.binaNo} Daire No: {self.daireNo}")
        
b1 = Bina(68)
b1.adresSoyle()

d1 = Daire(7,b1.binaNo)
d1.adresSoyle()









