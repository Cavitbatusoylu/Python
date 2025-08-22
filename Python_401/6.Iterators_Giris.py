# -*- coding: utf-8 -*-
sayilar = [2,5,7,8]

# for sayi in sayialr:
    # print(sayi)
    
sayilar = iter(sayilar)

print(sayilar.__next__())
print(sayilar.__next__())
print(sayilar.__next__())
print(sayilar.__next__())

sayilar = [2,5,7,8]

for sayi in sayilar:
    print(sayi)

sayilar = iter(sayilar)
print(20*"*")
print(next(sayilar))
print(next(sayilar))
print(next(sayilar))
print(next(sayilar))

# İlk 100 doğal sayıyı veren sınıf
class IlkYuzSayi:
    def __init__(self):
        self.sayi = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.sayi <= 100:
            sayi = self.sayi
            self.sayi += 1
            return sayi
        raise StopIteration
sayilar = IlkYuzSayi()
for i in range(10):
    print(next(sayilar))
    
sayilar = [1,2,3]
sayilar = iter(sayilar)
print(next(sayilar))
print(next(sayilar))
print(next(sayilar))
print(next(sayilar))
