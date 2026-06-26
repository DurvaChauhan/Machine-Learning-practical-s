#Write a Python program to implement k-Nearest Neighbour supervised machine learning algorithm for given dataset.
# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

# Features (X) and Target (y)
X = iris.data
y = iris.target

# Split dataset (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create KNN model (k = 3)
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print results
print("Predicted values:", y_pred)
print("Actual values:", y_test)
print("\nAccuracy of KNN model:", accuracy)