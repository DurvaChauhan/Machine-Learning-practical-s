#to sort the DataFrame first by 'name' in ascending order
import pandas as pd

data = {
    'name': ['Charlie', 'Alice', 'Bob'],
    'age': [35, 25, 30],
    'city': ['Paris', 'New York', 'London']
}
df = pd.DataFrame(data)

sorted_df = df.sort_values(by='name', ascending=True)
print(sorted_df)