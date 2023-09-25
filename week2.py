import pandas as pd


# print(pd.__version__) # check pandas version

df = pd.read_csv("housing.csv")


# print(df.isnull().any()) # check columns with missing data
print(df['population'].median())

# Splitting of dataset into the train, validation, and the test dataset 
n = len(df)

# Validation dataset
n_val = int(n * 0.2)

# Test dataset 
n_test = int(n * 0.2)

# Train dataset
n_train = n - n_val - n_test