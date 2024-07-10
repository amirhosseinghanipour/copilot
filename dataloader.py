import pandas as pd 
import os

def read_data(file_path):
    return pd.read_csv(file_path)

file_path = os.path.join("dataset", "train.csv")
data = read_data(file_path)
print(data.head())

data = data.applymap(lambda x: x.lower() if isinstance(x, str) else x)
data = data.fillna("No input data")
