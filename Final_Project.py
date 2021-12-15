import pandas
import matplotlib as mpl 
import matplotlib.pyplot as plt

df = pandas.read_csv('https://github.com/uncordingable/OSS-project.git/.csv')
print(df)
range_30 = list(range(30))
subset = df.iloc[range_30]
print(subset)
print(subset.groupby('Squad_Size')['Market_Value_Of_Club_In_Millions'].mean())

average_pay_by_Squad_Size = subset.groupby('Squad_Size')['Market_Value_Of_Club_In_Millions'].mean()

average_pay_by_Squad_Size.plot()

Top18_pay_by_Squad_Size=subset.groupby('Squad_Size')['Market_Value_Of_Top_18_Players_In_Millions'].mean()
print(Top18_pay_by_Squad_Size)

Top18_pay_by_Squad_Size.plot()
