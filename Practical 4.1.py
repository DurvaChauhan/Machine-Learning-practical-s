#to convert a NumPy array to a Pandas series
# Import libraries
import numpy as np
import pandas as pd

# Step 1: Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Step 2: Convert NumPy array to Pandas Series
series = pd.Series(arr)

# Step 3: Display the result
print("NumPy Array:")
print(arr)

print("\nConverted Pandas Series:")
print(series)