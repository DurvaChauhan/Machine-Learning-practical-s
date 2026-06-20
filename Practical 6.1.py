#to find and drop the missing values from the given dataset
import pandas as pd
df = pd.read_csv(r"C:\Users\ASUS\Desktop\Dataset\stocks.csv")
print(df)

d1 = df.copy()
for i in range (len(df)):
    if df.loc[i].isnull().any():
        d1 = df.drop(i)

print("Dataset after removing missing values:")
print(d1)