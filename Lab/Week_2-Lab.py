import pandas as pd
path = "A:\Semester 5\ML\Lab\Telco-Customer-Churn.csv"
df = pd.read_csv(path)

print(df.head())#first 5 rows

print(df.info())#information of the data

print(df.describe())#outliers exists

print(df.isnull())