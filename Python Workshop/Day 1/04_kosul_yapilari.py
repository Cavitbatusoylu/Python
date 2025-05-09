yas = 20
if yas >= 18:
    print("Reşit")
else:
    print("Reşit Değil")


not_ = 75
if not_ >= 90:
    print("AA")
elif not_ >= 80:
    print("BA")
elif not_ >= 70:
    print("BB")
else:
    print("Kaldiniz")


kullanici_adi = "admin"
sifre = "1234"
if kullanici_adi == "admin":
    if sifre == "1234":
        print("Giriş Başarili")
    else:
        print("Şifre Hatali")
else:
    print("Kullanici Adi Hatali")


yas = 20
ehliyet_var_mi = True
if yas >= 18 and ehliyet_var_mi:
    print("Araba Kullanabilirsiniz")
else:
    print("Araba Kullanamazsiniz")