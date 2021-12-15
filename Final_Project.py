import pandas
import matplotlib as mpl 
import matplotlib.pyplot as plt

df = pandas.read_csv('/workspace/malla/OSS-project/club.csv')
print(df)
range_30 = list(range(30))
subset = df.iloc[range_30]
print(subset)
print(subset.groupby('Squad_Size')['Market_Value_Of_Club_In_Millions'].mean())

average_pay_by_Squad_Size = subset.groupby('Squad_Size')['Market_Value_Of_Club_In_Millions'].mean()

average_pay_by_Squad_Size.plot()