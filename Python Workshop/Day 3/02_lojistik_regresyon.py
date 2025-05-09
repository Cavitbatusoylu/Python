import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

print ("Lojistik Regresyon Veri Seti Oluşturuluyor...")

data_classification = {
    "Age" : [22, 25, 47, 52, 46, 56, 55, 60, 62, 65],
    "Income" : [15000, 18000, 25000, 30000, 28000, 32000, 35000, 40000, 45000, 50000],
    "Purchased" : [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
}

df_classification = pd.DataFrame(data_classification)
print ("Lojistik Regresyon Veri Seti: ")
print(df_classification.head())

print("Lojistik Regresyon Veri Eğitim ve Test Setlerine Ayrılıyor...")

x_cls = df_classification[["Age", "Income"]]
y_cls = df_classification["Purchased"]

x_train, x_test, y_train, y_test = train_test_split(x_cls, y_cls, test_size=0.2, random_state=42)
print (f"Eğitim Seti Boyutu: {x_train.shape}")
print (f"Test Seti Boyutu: {x_test.shape}")

model = LogisticRegression()

model.fit(x_train, y_train)
print ("Lojistik Regresyon Modeli Eğitildi")
print("Katsayılar: ", model.coef_)
print("Kesim Noktası: ", model.intercept_)

print ("Lojistik Regresyon Model Test Verisi ile Tahmin yapılıyor...")

y_pred_cls = model.predict(x_test)

print ("Tahmin vs Gerçek Değerler:")
for gerçek, tahmin in zip(y_test, y_pred_cls):
    print(f"Gerçek: {gerçek}, Tahmin: {tahmin}")

print("Lojistik Regresyon Model Performansı Değerlendiriliyor...")

accuracy_score_cls = accuracy_score(y_test, y_pred_cls)

print(f"Doğrluk Skoru: {accuracy_score_cls:.4f}")


print("K-Nearest Neighbors Modeli Eğitiliyor...")
model_knn = KNeighborsClassifier(n_neighbors=3)

model_knn.fit(x_train, y_train)

print ("KNN Modeli Test Verisi ile Tahmin yapılıyor...")

y_pred_knn = model_knn.predict(x_test)
print ("Tahmin vs Gerçek Değerler:")

for gerçek, tahmin in zip(y_test, y_pred_knn):
    print(f"Gerçek: {gerçek}, Tahmin: {tahmin}")

print("KNN Model Performansı Değerlendiriliyor...")
accuracy_score_knn = accuracy_score(y_test, y_pred_knn)
print(f"Doğruluk Skoru: {accuracy_score_knn:.4f}")