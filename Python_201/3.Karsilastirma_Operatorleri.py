# -*- coding: utf-8 -*-

a = 10
b = 15
c = 20
d = 20

# ==
print(a == b)
print(c == d)
print(type(a == b))

# != eşit değil mi?
print(a != b) # True
print(c != d) # False

# > büyük mü?
print(a > b) # False
print(b > a) # True
print(c > d) # False

print("{} > {} sorusunun cevabı: {}".format(a,b,a > b))

# < küçük mü?
print(a < b) # True
print(b < a) # False
print(c < d) # False

# <= küçük mü ya da eşit mi?
print(a <= b) # True
print(b <= a) # False
print(c <= d) # True

# >= büyük mü ya da eşit mi?
print(a >= b) #False
print(b >= a) #True
print(c >= d) #True

#%% Stringlerle Karşılaştırma İşlemleri

isim = "Cavit"

print(isim == "Cavit") # True
print(isim != "Cavit") # False
print(isim == "Batu") # False
print(isim != "Batu") # True


# > sözlükte stringin sonra gelmesi
# < sözlükte stringin önce gelmesi

print("A" > "B") # False
print(ord("A"))
print(ord("B"))
print("A" < "B") # True

print("a" > "B") # True
print(ord("a"))
print(ord("B"))
print("a" < "B") # False

print("Ahmet" > "Ayşe") # False
print(ord("h"))
print(ord("y"))
print("Ahmet" < "Ayşe") # True

print("Ahmet" < "Ahmet")
print("Ahmet" > "Ahmet")
print("Ahmet" <= "Ahmet")
print("Ahmet" >= "Ahmet")

kelime1 = "ahmet" # a = 97
kelime2 = "Mehmet" # M = 77
print(ord("a"))
print(ord("M"))
print(kelime1 < kelime2)

kelime1 = kelime1.lower()
kelime2 = kelime2.lower()
print(kelime1, kelime2)

print(kelime1 < kelime2)