'''
Task: Geographic Analysis

1.Plot the locations of restaurants on a map using longitude and latitude coordinates.
2.Identify any patterns or clusters of restaurants in specific areas.
'''
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

read1 = pd.read_csv('Dataset.csv')
print(read1)

#Plot the locations of restaurants on a map using longitude and latitude coordinates.
print("\n----- Plot the locations of restaurants on a map using longitude and latitude coordinates -----")
plt.scatter(read1['Longitude'], read1['Latitude'])

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Restaurant Locations')

plt.show()



#Identify any patterns or clusters of restaurants in specific areas.
print("\n----- Identify any patterns or clusters of restaurants in specific areas -----")

# Assuming 'read1' is a DataFrame containing restaurant data with 'Longitude' and 'Latitude' columns

# Extracting the longitude and latitude columns
coordinates = read1[['Longitude', 'Latitude']]

# Specifying the number of clusters (you may need to adjust this based on your data)
num_clusters = 3

# Applying KMeans clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
read1['Cluster'] = kmeans.fit_predict(coordinates)

# Plotting the clustered restaurants
plt.scatter(read1['Longitude'], read1['Latitude'], c=read1['Cluster'], cmap='viridis')

# Adding labels and title
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Restaurant Clusters')

# Display the plot
plt.show()


