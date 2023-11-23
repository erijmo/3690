import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

url = 'https://raw.githubusercontent.com/erijmo/3690/main/CAR%20DETAILS%20FROM%20CAR%20DEKHO.csv'
df = pd.read_csv(url)

X = df[['year']]
y = df['selling_price']

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

X_test = np.arange(1992, 2021).reshape(-1, 1)
X_test_poly = poly.transform(X_test)
y_pred = model.predict(X_test_poly)

y_pred = np.maximum(y_pred, 0)

for year, pred in zip(X_test, y_pred):
    print(f'Prediction for year {int(year)}: {pred}')
