# -*- coding: utf-8 -*-

import sys
print("Şuanda Scriptimiz çalışıyor")

print(sys.argv)
print(type(sys.argv))
print(sys.argv[0])
print(sys.argv[1],type(sys.argv[1]))
print(sys.argv[2],type(sys.argv[2]))
print(sys.argv[3],type(sys.argv[3]))

sayi1,sayi2,sayi3 = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
sonuc = int(sys.argv[1]) + int(sys.argv[2]) + int(sys.argv[3])
print("Girilen argümanların toplamı: ",sonuc)

print("{} + {} + {} = {}".format(sayi1, sayi2, sayi3,sonuc))

