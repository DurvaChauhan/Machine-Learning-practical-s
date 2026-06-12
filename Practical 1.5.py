#to split an array of 14 elements into 3 arrays, each with 2, 4, and 8 elements in the original order
import numpy as np

arr = np.arange(1, 15)

arr1, arr2, arr3 = np.split(arr, [2, 6])

print("Original array:", arr)
print("First array (2 elements):", arr1)
print("Second array (4 elements):", arr2)
print("Third array (8 elements):", arr3)
