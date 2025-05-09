import numpy as np

print("Numpy Versiyonu:", np.__version__)

liste = [1, 2, 3, 4, 5]
numpy_dizi = np.array(liste)
print("Türü:", type(numpy_dizi))

numpy_dizi2 = np.array([10, 20, 30, 40, 50, 60])
print("Dizi 2:", numpy_dizi2)

dizi_aralik = np.arange(0, 10, 2)
print("Aralık Numpy Dizisi:", dizi_aralik)

dizi_sifirlar = np.zeros(5) 
print("Sıfır Numpy Dizisi:\n", dizi_sifirlar)

dizi_birler = np.ones(5) 
print("Bir Numpy Dizisi:\n", dizi_birler)

dizi_linspace = np.linspace(0, 20, 5)
print("Eşit Parça Numpy Dizisi:", dizi_linspace)

dizi_random = np.random.rand(5)  # 0 ile 1 arasında rastgele 5 sayı
print("Rastgele Numpy Dizisi:", dizi_random)

dizi = np.array(10,20,30,40,50)

print("Dizi:", dizi)
print("Toplam:", np.sum(dizi))
print("Ortalama:", np.mean(dizi))
print("Maksimum:", np.max(dizi))
print("Minimum:", np.min(dizi))
print("Standart Sapma:", np.std(dizi))
print("Varyans:", np.var(dizi))

matris = np.random.randint(1, 10, (2, 3))
print("Matris:\n", matris)

transpoz = matris.T
print("Transpoze Matris:\n", transpoz)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
carpim = np.dot(A, B)
print("Matris Çarpımı:\n", carpim)