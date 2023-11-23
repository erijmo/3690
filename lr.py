import pandas as pd
import numpy as np

github_csv_url = ''

df = pd.read_csv(github_csv_url)

X = df['year'].values
y = df['selling_price'].values

mean_X = np.mean(X)
mean_y = np.mean(y)

numerator = np.sum((X - mean_X) * (y - mean_y))
denominator = np.sum((X - mean_X) ** 2)
beta = numerator / denominator
alpha = mean_y - beta * mean_X

X_test = np.arange(1992, 2021)
y_pred = alpha + beta * X_test


print(f'Slope (beta): {beta}')
print(f'Intercept (alpha): {alpha}')

for year, pred in zip(X_test, y_pred):
    print(f'Prediction for year {year}: {pred}')
