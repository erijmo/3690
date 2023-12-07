import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/erijmo/3690/main/Credit%20Card%20Customer%20Data.csv"
customer_data = pd.read_csv(url)

selected_features = ['Avg_Credit_Limit', 'Total_Credit_Cards']
customer_data_selected = customer_data[selected_features].dropna()

kmeans = KMeans(n_clusters=3, random_state=6)
customer_data_selected['cluster'] = kmeans.fit_predict(customer_data_selected)

cluster_centers = kmeans.cluster_centers_

plt.scatter(customer_data_selected['Avg_Credit_Limit'], customer_data_selected['Total_Credit_Cards'], c=customer_data_selected['cluster'], cmap='viridis', edgecolors='k')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=80, c='red', marker='^')
plt.title('Customer Segmentation')
plt.xlabel('Average Credit Limit')
plt.ylabel('Total Credit Cards')
plt.show()

print("Cluster Center Coordinates:")
print(cluster_centers)
