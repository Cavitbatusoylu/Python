try:
    sayi = int(input("Bir sayı girin: "))
    print(10/sayi)
except ValueError:
    print("Lutfen sadece sayi girin")
except ZeroDivisionError:
    print("Sıfıra bölme hatasi")
except Exception as e:
    print("Beklenmeyen bir hata oluştu:", e)
else:
    print("Başarıyla bölündü")
finally:
    print("İşlem tamamlandı")
