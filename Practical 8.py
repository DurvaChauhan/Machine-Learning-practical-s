#Write a Python program to read csv file and using Scikit-learn to print the keys, number of rows columns, shape, top 5 rows, feature names and the description of the given data. 
import sklearn
from sklearn.datasets import load_iris
import pandas as pd

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

# Convert to DataFrame
df = pd.DataFrame(X, columns=feature_names)

# 1. Keys
print("Keys:")
print(iris.keys())

# 2. Number of rows and columns
print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# 3. Shape
print("\nShape of Dataset:")
print(df.shape)

# 4. Top 5 rows
print("\nTop 5 Rows:")
print(df.head())

# 5. Feature Names
print("\nFeature Names:")
print(feature_names)

# 6. Target Names
print("\nTarget Names:")
print(target_names)

# 7. Description
print("\nDataset Description:")
print(iris.DESCR)