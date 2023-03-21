# Which Professor takes the highest and lowest salaries?

import pandas as pd
df = pd.read_csv('Salaries.csv')

prof_data = df.query('rank == "Prof"')
high_sal = prof_data.salary.max()
low_sal = prof_data.salary.min()
print("Maximum salary of a professor:",high_sal)
print("Minimum salary of a professor:",low_sal)