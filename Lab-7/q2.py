# # Display how many rows and how many columns and Display first 10 rows and
# last 15 rows.

import pandas as pd

salaries = pd.read_csv("Salaries.csv")

result = salaries.head(10)
print("First 10 rows are:\n", result)

result2 = salaries.tail(15)
print("\nLast 15 rows:\n", result2)