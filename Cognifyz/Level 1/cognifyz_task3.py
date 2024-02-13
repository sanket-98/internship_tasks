'''

Task: Price Range Distribution

1.Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants.
2.Calculate the percentage of restaurants in each price range category.

'''
import pandas as pd
from matplotlib import pyplot as plt

read1 = pd.read_csv('Dataset.csv')
print(read1)

#Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants.
print("\n----- Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants -----")
plt.hist(read1['Price range'])
plt.show()


#Calculate the percentage of restaurants in each price range category.
print("\n----- Calculate the percentage of restaurants in each price range category -----")
percentage = round(read1['Price range'].dropna().value_counts() / len(read1['Price range'].dropna()) * 100, 2)
print(percentage)







