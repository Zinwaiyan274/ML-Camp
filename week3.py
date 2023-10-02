import pandas as pd



data = pd.read_csv("data.csv")
# print(data.head())          


# Check the frequency of the 'color' column
frequency_checking = data['Transmission Type'].value_counts()
# print(frequency_checking)



# Select columns to calculate coor
df_col = data[['Engine HP', 'Year', "Engine Cylinders", "highway MPG", "city mpg"]]


print(df_col.corr(method='pearson', min_periods=1) )