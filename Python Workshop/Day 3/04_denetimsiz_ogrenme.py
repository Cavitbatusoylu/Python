import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

data = pd.read_csv("Mall_Customers.csv")

x = data[["Annual Income (k$)", "Spending Score (1-100)"]]

print(x.head())

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", n_init=10, random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title("Elbow Method")
plt.xlabel("Number of clusters")
plt.ylabel("WCSS")
plt.grid(True)
plt.show()

kmenas = KMeans(n_clusters=5, init="k-means++", random_state=42)

clusters = kmeans.fit_predict(x)
data["Cluster"] = kmeans.fit_predict(x)

plt.figure(figsize=(8, 6))
color  = ["red", "blue", "green", "cyan", "magenta"]

for i in range(5):
    plt.scatter(x[data["Cluster"] == i]["Annual Income (k$)"],
                x[data["Cluster"] == i]["Spending Score (1-100)"],
                s=100, c=color[i], label=f"Cluster {i+1}")
    plt.scatter(kmeans.cluster_centers_[i][0], kmeans.cluster_centers_[i][1],
                s=300, c="yellow", marker="*", label= "Merkezler", marker = 'X')
    plt.xlabel("Yıllık Geliri (k$)")
    plt.ylabel("Harcamalar Skoru (1-100)")
    plt.title("Müşteri Segmentasyonu")
    plt.legend()
    plt.grid(True)
    plt.show()