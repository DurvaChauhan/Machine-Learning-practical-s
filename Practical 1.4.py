#to create another shape from an array without changing its data (3*2 to 2*3)  
import numpy as np
arr = np.array([[1, 2],
               [3, 4],
               [5, 6]])

print("Original Array:")
print(arr)

changed_array = arr.reshape(2, 3)

print("\nDifferent Shaped Array")
print(changed_array)