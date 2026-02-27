import pandas as pd


df = pd.read_csv('C:\\Users\\shrey\\SHLOK Python Code\\5_Days_Data_Analytics_Bootcamp\\day_4\\Indian_employee_dataset - Sheet1.csv')

print(df.head())


print(df.columns)


print(df['Salary (LPA)'].mean())


print(df['Salary (LPA)'].max())


print(df['Salary (LPA)'].min())

max_salary = df['Experience'].max()



print(df['Experience'].min())