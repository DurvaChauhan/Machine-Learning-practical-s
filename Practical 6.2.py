#to remove the duplicates from the given dataset
import pandas as pd
import numpy as np
data = pd.read_csv(r"C:\Users\ASUS\Desktop\Dataset\stocks.csv")
print(data)

d1 = data.drop_duplicates()
print("Dataset after removing duplicates :")
print(d1)