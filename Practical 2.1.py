#to add, subtract, multiply, divide arguments element-wise
import numpy as np

# Create two NumPy arrays
a = np.array([60, 70, 80, 90])
b = np.array([2, 4, 5, 8])

# Element-wise operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

# Display results
print("Array A:", a)
print("Array B:", b)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
