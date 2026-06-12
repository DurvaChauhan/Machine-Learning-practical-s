#to stack arrays horizontally (column wise)
import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Stack arrays horizontally (column-wise)
result = np.column_stack((arr1, arr2))

# Display the result
print("First array:", arr1)
print("Second array:", arr2)
print("Horizontally stacked array:")
print(result)
