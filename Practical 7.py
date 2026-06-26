#Write a Pandas program to create a line plot of the opening, closing stock prices of given company between two specific dates.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stocks.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Check your actual dates
print(df['Date'])

# Filter (make sure dates match your file)
data = df[(df['Date'] >= '2023-01-01') & (df['Date'] <= '2023-01-10')]

print(data)  # IMPORTANT

# Plot only if data exists
if not data.empty:
    plt.plot(data['Date'], data['Open'], label='Open')
    plt.plot(data['Date'], data['Close'], label='Close')
    plt.legend()
    plt.show()
else:
    print("No data found in this date range ❌")
