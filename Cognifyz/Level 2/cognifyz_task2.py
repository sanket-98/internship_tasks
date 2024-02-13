'''
Task: Cuisine Combination

1.Identify the most common combinations of cuisines in the dataset.
2.Determine if certain cuisine combinations tend to have higher ratings.

'''
import pandas as pd

read = pd.read_csv('Dataset.csv')
print(read)

#Identify the most common combinations of cuisines in the dataset.
print("\n----- Identify the most common combinations of cuisines in the dataset -----")
most_common_combination = read['Cuisines'].value_counts()
print(most_common_combination)
print('The most common combination of cuisines is :',read['Cuisines'].value_counts().idxmax())


#Determine if certain cuisine combinations tend to have higher ratings.
print("\n----- Determine if certain cuisine combinations tend to have higher ratings -----")
average_rating_by_cuisine = read.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
print(average_rating_by_cuisine)