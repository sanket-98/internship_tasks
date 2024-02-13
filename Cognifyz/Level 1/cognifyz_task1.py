'''
Task: Top Cuisines

1.Determine the top three most common cuisines in the dataset.
2.Calculate the percentage of restaurants that serve each of the top cuisines.

'''
import pandas as pd

read = pd.read_csv('Dataset.csv')
print(read)

#Determine the top three most common cuisines in the dataset.
print(("----- Determine the top three most common cuisines in the dataset -----"))
top_cuisines = read['Cuisines'].value_counts().head(3)
print(top_cuisines)

#Calculate the percentage of restaurants that serve each of the top cuisines.
print(("----- Calculate the percentage of restaurants that serve each of the top cuisines -----"))
percentage = round(read['Cuisines'].value_counts() / len(read) * 100, 2)
print(percentage)
