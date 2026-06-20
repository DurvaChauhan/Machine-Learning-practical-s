#drop rows with any NaNs
import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\ASUS\Desktop\Dataset\stocks.csv")
print(data)

d1 = data.dropna()

print(d1)