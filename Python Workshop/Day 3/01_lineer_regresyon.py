import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


print("Veri seti oluşturuluyor...")

data = {
    "TV" : [230,44,17,151,180,8,57,120,100,220],
    "Radio" : [37,39,45,41,10,8,12,19,24,30],
    "Newspaper" : [69,21,14,23,10,7,5,19,20,25],
    "Sales" : [22,10,7,11,12,4,5,7,8,18]
}

df = pd.DataFrame(data)

print ("Linear Regresyon Veri Seti: ")
print(df.head())

print ("Veri Eğitim ve Test Setlerine Ayrılıyor...")

x = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print (f"Eğitim Seti Boyutu: {x_train.shape}")
print (f"Test Seti Boyutu: {x_test.shape}")

print ("Linear Regresyon Modeli Eğitiliyor...")

model = LinearRegression()

model.fit(x_train, y_train)

print ("Lineer Regresyon Model Eğitildi.")
print ("Modelin Katsayıları: ", model.coef_)
print ("Modelin Kesim Noktası: ", model.intercept_)

print ("Model Test Verisi ile Tahmin yapılıyor...")

y_pred = model.predict(x_test)

print("Tahmin vs Gerçek Değerler:")

for gerçek, tahmin in zip(y_test, y_pred):
    print(f"Gerçek: {gerçek}, Tahmin: {tahmin:.2f}")

print ("Model performansı değerlendiriliyor...")

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print ("Model Performansı Sonuçları:")
print (f"MSE: {mse:.4f}")
print (f"R^2 Skoru: {r2:.4f}")

plt.scatter(y_test, y_pred, color = "blue")
plt.xlabel("Gerçek Değerler")
plt.ylabel("Tahmin Değerleri")
plt.title("Lineer Regresyon")
plt.grid(True)

plt.savefig("lineer_regresyon.png")
plt.show()