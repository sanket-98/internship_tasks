'''
Task: City Analysis

1.Identify the city with the highest number of restaurants in the dataset.
2.Calculate the average rating for restaurants in each city.
3.Determine the city with the highest average rating.

'''
import pandas as pd

read1 = pd.read_csv('Dataset.csv')
print(read1)

#Identify the city with the highest number of restaurants in the dataset.
print("\n----- Identify the city with the highest number of restaurants in the dataset -----")
city = read1['City'].value_counts().idxmax()
print(city)

#Calculate the average rating for restaurants in each city.
print("\n----- Calculate the average rating for restaurants in each city -----")
avg_ratings_by_city = read1.groupby('City')['Aggregate rating'].mean().round(2)
print(avg_ratings_by_city)


#Determine the city with the highest average rating.
print("----- Determine the city with the highest average rating -----")
max_rating_row = read1.loc[read1['Aggregate rating'].idxmax()]
print(max_rating_row)
