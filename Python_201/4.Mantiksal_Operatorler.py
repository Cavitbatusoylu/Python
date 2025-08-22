# -*- coding: utf-8 -*-

onerme1 = "Real Madrid bir futbol takımıdır"
onerme2 = "Galatasaray dünyanın en iyi futbol takımıdır"
onerme3 = "Fenerbahçe bir futbol takımıdır"
onerme4 = "Fenerbahçe dünyanın en iyi futbol takımı değildir"

o1 = True  #1  # not o1 = False
o2 = False #0  # not o2 = True
o3 = True  #1
o4 = False #0

# or and not

# OR TABLOSU
# or | o1 o2 | s
#-----------------
#    | 0   0 | 0
#    | 0   1 | 1
#    | 1   0 | 1
#    | 1   1 | 1

# AND TABLOSU
# and | o1 o2 | s
#-----------------
#     | 0   0 | 0
#     | 0   1 | 0
#     | 1   0 | 0
#     | 1   1 | 1

# NOT TABLOSU
# not | o | s
#-------------
#     | 1 | 0
#     | 0 | 1

#%%

a = 10
b = 15

a, b = 10, 15
c, d, e = 20, 25, 30

print("OR")
print(a < 15 or b < 20)
print("{} or {} = {}".format(a < 15, b < 20, a < 15 or b < 20))
print("{} or {} = {}".format(a < 10, b < 20, a < 10 or b < 20))
print("{} or {} = {}".format(a < 15, b < 15, a < 15 or b < 15))
print("{} or {} = {}".format(a < 10, b < 15, a < 10 or b < 15))

print("AND")
print("{} and {} = {}".format(a < 15, b < 20, a < 15 and b < 20))
print("{} and {} = {}".format(a < 10, b < 20, a < 10 and b < 20))
print("{} and {} = {}".format(a < 15, b < 15, a < 15 and b < 15))
print("{} and {} = {}".format(a < 10, b < 15, a < 10 and b < 15))

print("NOT")
anahtar = True
print(anahtar)
anahtar = not anahtar
print(anahtar)

sonuc = not (a < 15 and b < 20 or c < 25 and d < 30)
#sonuc = not (True and True or True and True)

#%% 

k1 = 4 < 5
k2 = 5 > 6
k3 = 7 <= 7

print(k1, k2, k3)

sonuc1 = bool("Ahmet") # True
sonuc2 = bool(5)       # True
sonuc3 = bool(4.8)     # True

import sys
print(sys.getsizeof(5))
print(28*8)
#000..00101

print(ord("A"))

sonuc4 = bool("")  # False
sonuc5 = bool(0)   # False
sonuc6 = bool(0.0) # False
sonuc7 = bool(" ") # True
print(ord(" "))

#%% Tek Terimli Operatörler

# + - ~

x = +-+--12
y = ---x

z = ++++++++++++++15
print(z)
z = -z
print(z)

# bitwise (bit bazında operatör)

t = 5 # 0101 # işaret bitleri 0 pozitif 1 negatif
m = ~t #(0101)' = 1010

# -A = A' + 1
# A' = -A - 1
#    = 1010 - 0001
#    = 1001
# A = (A')' = (1001)' = 0110 = ONLUK TABANDA +6

#%% Benzerlik Operatörleri

# is  is not

x = 5
y = 5.0

#type() value(değer)
print(x is y) # False
print("x: ",type(x),x)
print("y: ",type(y),y)

print(x == y) # True

print(x is not y) # True
print(x != y) # False

k1 = 2 < 3 #bool, True
print((2 < 3) is True) # True
print(type(2 < 3),2 < 3)
print(type(True),True)

print("5 5'e hem tip hem de değer bakımından eşit mi? ", type(5) == type(5) and 5 == 5)

#%% Bitwise (Bitsel) Operatörler

# & (bitwise and)
# | (bitwise or)
# ~ (bitwise not)(Complement-Tümleyeni)
# ^ (bitwise xor)
# >> (bitwise right shift)
# << (bitwise left shift)

x = 15 # 1111
y = 10 # 1010

sonuc1 = x & y # 1010 = ONLUK TABANDAKİ KARŞILIĞI 10

x = 11 # 1011
y = 10 # 1010

sonuc2 = x | y # 1011

z = 5
sonuc3 = ~z

sonuc4 = x ^ y # 0001

t = 7 # 111 => 001
t >>= 2

p = 3 # 11 => 1100
p <<= 2

#%% Membership (Üyelik) Operatörleri

# in   not in

kelime1 = "Türkiye"
print("ü" in kelime1)
print("t" in kelime1)
print("ye" in kelime1)
print("ey" in kelime1)

liste = [1,2,3]

print(1 in liste)
print(2 in liste)
print(3 in liste)
print(4 in liste)

print("g" not in kelime1) # True
print(5 not in liste) # True

print("r" not in kelime1) # False
print(3 not in liste) # False













