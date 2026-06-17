#to delete the one specific column from the DataFrame 
import pandas as pd

data = {
    'name': ['Durva', 'Hani', 'Khushi'],
    'age': [8, 72, 24],
    'city': ['New York', 'Paris', 'England']
}

df = pd.DataFrame(data)
updated_df = df.drop(columns=['city'])

print(df)
print(updated_df)