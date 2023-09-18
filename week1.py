import pandas as pd


# print(pd.__version__) # check pandas version

df = pd.read_csv("housing.csv")
# print(df.head())


# print(df.isnull().any()) # check columns with missing data
# print(df["total_bedrooms"])

# print(df["ocean_proximity"].unique())
# print(df['median_house_value'].mean())




# print(df["total_bedrooms"].isna().sum()) # To get the total number of rows with missing data, sum the values in the Series
# print(df['total_bedrooms'].fillna(df['total_bedrooms'].median(), inplace=True))
# print(df["total_bedrooms"].isna().sum()) 
print(df['ocean_proximity'].str.contains('w'))
