#to calculate mean across dimension, in a 2D numpy array 
import numpy as np

# Create a 2D NumPy array
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

# Mean across rows (row-wise mean)
mean_rows = np.mean(arr, axis=1)

# Mean across columns (column-wise mean)
mean_columns = np.mean(arr, axis=0)

# Mean of all elements
mean_all = np.mean(arr)

# Display results
print("Array:\n", arr)
print("Mean across rows:", mean_rows)
print("Mean across columns:", mean_columns)
print("Mean of all elements:", mean_all)
