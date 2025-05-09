import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.metrics import confusion_matrix, classification_report

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

tree_model = DecisionTreeClassifier()
tree_model.fit(x_train, y_train)
tree_pred = tree_model.predict(x_test)
print("Karar Ağacı Doğruluğu: ", accuracy_score(y_test, tree_pred))

forest_model = RandomForestClassifier()
forest_model.fit(x_train, y_train)
forest_pred = forest_model.predict(x_test)
print("Random Forest Doğruluğu: ", accuracy_score(y_test, forest_pred))

svm_model = SVC()
svm_model.fit(x_train, y_train)
svm_pred = svm_model.predict(x_test)
print("SVM Doğruluğu: ", accuracy_score(y_test, svm_pred))

new_flower = np.array([[5.1, 3.5, 4.5, 1.7]])
prediction_tree = tree_model.predict(new_flower)
print("Karar Ağacı ile Tahmin: ", iris.target_names[prediction_tree][0])

prediction_forest = forest_model.predict(new_flower)
print("Random Forest ile Tahmin: ", iris.target_names[prediction_forest][0])

prediction_svm = svm_model.predict(new_flower)
print("SVM ile Tahmin: ", iris.target_names[prediction_svm][0])

x_petal = x[:, [2, 3]]
for label, color, species in zip([0, 1, 2], ['red', 'blue', 'green'], iris.target_names):
    plt.scatter(x_petal[y == label, 0], x_petal[y == label, 1], c=color, label=species)

plt.xlabel("Petal Uzunluğu")
plt.ylabel("Petal Genişliği")
plt.title("Iris Türlerinin Petal Uzunluğu ve Genişliği")
plt.legend()
plt.grid(True)
plt.show()

cm = confusion_matrix(y_test, tree_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap=plt.cm.Blues)
plt.title("Karar Ağacı - CM")
plt.show()

report = classification_report(y_test, tree_pred, target_names=iris.target_names)
print("Karar Ağacı - Sınıflandırma Raporu:\n", report)
