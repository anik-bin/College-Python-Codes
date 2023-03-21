# Which Male and Female Professor has the highest and the lowest salaries?

import pandas as pd
df = pd.read_csv('Salaries.csv')

print("Max Salary")
print(df.groupby('sex').apply(lambda x: x[x['salary'] == x['salary'].max()]))

print("Min Salary")
print(df.groupby('sex').apply(lambda x: x[x['salary'] == x['salary'].min()]))