'''
Task: Restaurant Chains

1.Identify if there are any restaurant chains present in the dataset.
2.Analyze the ratings and popularity of different restaurant chains.
'''
import pandas as pd

read1 = pd.read_csv('Dataset.csv')
print(read1)

#Identify if there are any restaurant chains present in the dataset.
print("\n----- Identify if there are any restaurant chains present in the dataset -----")
chains = read1['Restaurant Name'].value_counts()
# Filter chains with more than one location
chains = chains[chains > 1]

# Print the filtered list of chains
print("Restaurant Chains:")
print(chains)

# Analyze the ratings and popularity of different restaurant chains.
print("\n----- Analyze the ratings and popularity of different restaurant chains -----")

# Create a new dataframe with only the chains with more than one location
chains_df = read1[read1['Restaurant Name'].isin(chains.index)]

# Calculate the average rating for each chain
avg_ratings_by_chain = chains_df.groupby('Restaurant Name')['Aggregate rating'].mean().round(2)

# Print the average rating for each chain
print("Average Ratings by Chain:")
print(avg_ratings_by_chain)
