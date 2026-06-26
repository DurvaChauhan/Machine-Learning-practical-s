#Write a Python program that uses Scikit-learn to split a dataset into training and testing sets using train_test_split.
# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
iris = load_iris()

# Features (X) and Target (y)
X = iris.data
y = iris.target

# Split dataset into training and testing sets
# 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Print results
print("Total data:", len(X))
print("Training data:", len(X_train))
print("Testing data:", len(X_test))

print("\nShape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of y_test:", y_test.shape)