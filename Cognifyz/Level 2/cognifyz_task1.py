'''
Task: Restaurant Ratings

1.Analyze the distribution of aggregate ratings and determine the most common rating range.
2.Calculate the average number of votes received by restaurants.
'''

import pandas as pd
from matplotlib import pyplot as plt

read1 = pd.read_csv('Dataset.csv')
print(read1)

#Analyze the distribution of aggregate ratings and determine the most common rating range.
print("\n----- Analyze the distribution of aggregate ratings and determine the most common rating range -----")

# Define rating bins (0-1, 1-2, 2-3, 3-4, 4-5)
bins = [i for i in range(6)]
rating_ranges = [f"{i}-{i+1}" for i in range(5)]

# Create a new column with rating ranges
read1['Rating Range'] = pd.cut(read1['Aggregate rating'], bins=bins, labels=rating_ranges, include_lowest=True)

# Find the most common rating range
most_common_rating_range = read1['Rating Range'].value_counts().idxmax()
print(f"Most common rating range: {most_common_rating_range}")

#Calculate the average number of votes received by restaurants.

print("\n----- Calculate the average number of votes received by restaurants -----")
avg_votes_by_city = read1.groupby('Restaurant Name')['Votes'].mean()
print(avg_votes_by_city)



