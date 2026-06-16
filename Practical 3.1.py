#to find the maximum and minimum value of a given flattened array 
import numpy as np

# Create a NumPy array (2D example)
arr = np.array([[10, 45, 3],
                [22, 8, 60]])

# Flatten the array
flat_arr = arr.flatten()

# Find maximum and minimum values
max_value = np.max(flat_arr)
min_value = np.min(flat_arr)

# Display results
print("Original Array:\n", arr)
print("Flattened Array:", flat_arr)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
