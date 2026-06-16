#to compute the mean, standard deviation, and variance of a given array along the second axis 
import numpy as np

# Create a 2D NumPy array
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

# Compute statistics along the second axis (row-wise)
mean_val = np.mean(arr, axis=1)
std_dev = np.std(arr, axis=1)
variance = np.var(arr, axis=1)

# Display results
print("Array:\n", arr)
print("Mean along second axis:", mean_val)
print("Standard Deviation along second axis:", std_dev)
print("Variance along second axis:", variance)
