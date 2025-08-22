# -*- coding: utf-8 -*-

"""Errors (Hatalar)"""
# Exception (Olağandışılık, istisna)
# Handling (İşleme, idare etme)

#1-) Compile time errors (Derleme zamanında hataları)
    # Syntactical Errors (Dil bilgisi hataları)
        # ; işaretini for veya if'in sonuna koymamak gibi hatalar.

#2-) Logical errors (Mantıksal Hatalar)
    # Wrong output (Yanlış çıktı)
        # Fonksiyona 5 ve 6 sayılarını gönderiyorsun
        # ama sonuç olarak 10 çıkıyor
        # 11 çıkmıyor gibi hatalar. (Mantıksal Hatalar)

#3-) Run time errors (Çalışma zamanında hatalar)
    # Divide by zero (Sıfıra bölme)
        # Bir sayıyı 0'a böldüğümüz zamanki gibi çıkan hatalar.

# Statement
    # Normal (Warning - Uyarı)
    # Critical (Error - Hata)

#%% 
# ValueError (Değer Hatası)
# ZeroDivisionError (Sıfıra Bölme Hatası)

try:
    #raise ValueError
    sayi1 = int(input("Lütfen bir tamsayı giriniz: "))
    sayi2 = int(input("Lütfen bir tamsayı giriniz: "))
    print(f"{sayi1}/{sayi2} = {round(sayi1/sayi2,4)}")
except ValueError:
    print("Lütfen tamsayı giriniz")
except ZeroDivisionError:
    print("Hiçbir reel sayı sıfıra bölünemez! Lütfen 2.sayıyı 0 dan farklı bir değer giriniz")

#%%
sayi1 = 9
sayi2 = 0

try:
    sayi2 = int(input("Sayı gir: "))
    print(sayi1/sayi2)
except Exception as e:
    print("Karşılaşılan Hata:", e)


#%% 
sayi1 = 10
sayi2 = 0
try:
    print("Dosya açıldı!")
    print(sayi1/sayi2)
except Exception as e:
    print("Hata: ", e)
finally:
    print("Dosya kapandı!")

#%% 
def fact(n):
    if n < 0 or type(n) != int:
        raise ValueError("Sayı doğal sayı olmalıdır!")
    if n == 0:
        return sayi1
    return n * fact(n-1)

try:
    print(fact(6))
    print(fact(-6))
except Exception as e:
    print("Hata: ", e)































