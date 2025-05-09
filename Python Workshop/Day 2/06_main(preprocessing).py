from preprocessing import handle_missing_values, encode_categorical_data, scale_data, split_data

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


if __name__ == "__main__":

    # Veri setini yükle
    data = pd.DataFrame({
        "Yaş": [25, 45, 30, 35, 40],
        "Cinsiyet": ["K", "E", "K", "E", None],
        "Maaş": [6000, 8000, None, 9000, 7500],
        "Deneyim": [2, 20, 5, 10, 15],
        "Departman": ["IT", "HR", "Yönetim", "Muhasebe", "Yönetim"],
        "Terfi": [0, 1, 0, 1, 0],
    })

    data = handle_missing_values(data)

    data = encode_categorical_data(data)

    scaler = StandardScaler()

    data[["Yaş", "Maaş", "Deneyim"]] = scaler.fit_transform(data[["Yaş", "Maaş", "Deneyim"]])
    x = data.drop("Terfi", axis=1)
    y = data["Terfi"]

    x_train, x_test, y_train, y_test = split_data(data)

    model = LogisticRegression()

    model.fit(x_train, y_train)

    new_employee = pd.DataFrame({
        "Yaş": [28],
        "Cinsiyet": ["K"],
        "Maaş": [7000],
        "Deneyim": [3],
        "Departman_IT": [1],
        "Departman_Muhasebe": [0],

    })

    new_employee[["Yaş", "Maaş", "Deneyim"]] = scaler.transform(new_employee[["Yaş", "Maaş", "Deneyim"]])

    prediction = model.predict(new_employee)

    if prediction[0] == 1:
        print("Bu çalışan terfi alabilir.")
    else:
        print("Bu çalışan terfi alamaz.")