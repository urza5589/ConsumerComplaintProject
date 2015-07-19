import pandas as pd

data_file = 'Consumer_Complaints.csv'

df = pd.read_csv(data_file, header=0)

print(df.head(5))