import pandas as pd
df = pd.read_csv('Salaries.csv')

s = list(df[df['phd'].isnull()]['service'])
filtered_data = df.query('service == 18 or service == 2 ')
print(filtered_data)
filtered_data = filtered_data.fillna(filtered_data.mean())
print(filtered_data)