#to write a DataFrame to CSV file using tab separator
import pandas as pd

path = r'C:\Users\ASUS\Desktop\Dataset\lamborghini_sales_2020_2025.csv'
df = pd.read_csv(path)
print(df.head())
