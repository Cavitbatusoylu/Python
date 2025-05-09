import math as a
from math import sqrt, factorial
import random as r
import requests
import mat_modul

print(a.sqrt(16))
print(a.factorial(5))

print(r.randint(1, 10))

try:
    icerik = requests.get("https://jsonplaceholder.typicode.com/")
    print(icerik.json())
except Exception as e:
    print("İstek sırasında hata oluştu:", e)

print(mat_modul.topla(5, 10))
print(mat_modul.carp(5, 10))
