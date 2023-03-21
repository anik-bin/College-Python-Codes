import pandas as pd

# list1 = ['CSE', 'IT', 'CSCE', 'ELE']

# branch = pd.Series(list1, index=['C', 'I', 'CS', 'E'])

# print(branch)

# # data frame

# dict1 = {
#     "Roll": [1, 2, 3, 4, 5],
#     "Subject": ["Science", "Maths", "Physics", "History", "Geography"]
# }

# subjects = pd.DataFrame(dict1)

# print(subjects)
# print(subjects.loc[0])

# df = pd.read_csv("Salaries.csv")
# print(df.shape) # read row and columns

# check dimensions

# print(df.ndim)

# print(df.columns)

# print(df.columns.to_list)

# print(df.head())

# print(df.tail())

# randomly display 4 rows

# print(df.sample(5))

# print(df.columns)

# print(df['rank'])

# print(df['rank'].value_counts())

# print(df['discipline'].unique)

# print(df['discipline'].value_counts())

# print(df[['rank','discipline']])

# print(df[['rank','discipline','service']])

# print(df.isnull().sum())