#to convert the first column of a DataFrame as a Series
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [40, 50, 60]
})

# Convert the first column to a Series
first_column_series = df.iloc[:, 0]

print(first_column_series)
print(type(first_column_series))