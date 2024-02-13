'''
Task: Online Delivery

1.Determine the percentage of restaurants that offer online delivery.
2.Compare the average ratings of restaurants with and without online delivery.

'''
import pandas as pd
from matplotlib import pyplot as plt

read1 = pd.read_csv('Dataset.csv')
print(read1)

#Determine the percentage of restaurants that offer online delivery.
print("\n----- Determine the percentage of restaurants that offer online delivery -----")
online_delivery_percentage = round((read1['Has Online delivery'] == 'Yes').sum() / len(read1) * 100, 2)
print(f"Percentage of restaurants offering online delivery: {online_delivery_percentage}%")

#Compare the average ratings of restaurants with and without online delivery.
print("\n----- Compare the average ratings of restaurants with and without online delivery -----")
avg_ratings_by_city = read1.groupby('Has Online delivery')['Aggregate rating'].mean().round(2)
print(avg_ratings_by_city)


