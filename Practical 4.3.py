#to create the mean and standard deviation of the data of a given Series
import pandas as pd

# Example Series
s = pd.Series([10, 20, 30, 40, 50])

# Mean
mean_value = s.mean()

# Standard Deviation
std_value = s.std()

print("Mean:", mean_value)
print("Standard Deviation:", std_value)