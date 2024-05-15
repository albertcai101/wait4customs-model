import pandas as pd

# list all unique "Airport" in the dataset.csv
def airport_list():
    df = pd.read_csv('dataset.csv')
    return df['Airport'].unique()

# print the list of airports
print(airport_list())