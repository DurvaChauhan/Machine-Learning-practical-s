#to calculate the difference between neighboring elements, element-wise of a given array 
import numpy as np

# Create a NumPy array
arr = np.array([10, 15, 25, 40, 60])

# Calculate difference between neighboring elements
diff = np.diff(arr)

# Display results
print("Original Array:", arr)
print("Difference between neighboring elements:", diff)
