#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:12:30 2024

@author: dianachapter
"""

import pandas as pd 

#file= pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
#url = "https://raw.githubusercontent.com/kode2go/nithecs/main/lecture_01/iris.csv"
#file = pd.read_csv(url)
file = pd.read_csv("data_02/Geospatial Data.txt", sep=";")
file = pd.read_excel("data_02/residentdoctors.xlsx")
file = pd.read_json("data_02/student_data.json")


url ="https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

# DataFrame

# df = pd.read_csv(url)

# print(df.info())
# print(df.describe())

#df = pd.read_csv("chat_file/Accelerometer_data.csv", names = ["data_time","x","y","z"])

#df = pd.read_csv("data_02/country_data_index.csv",index_col=0)
# df = pd.read_excel("data_02/residentdoctors.xlsx")

# df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')
# print(df.info())

# df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)
# print(df.info())

"""
Working with dates
30-01-2024
01-30-2024
"""

df = pd.read_csv("data_02/time_series_data.csv", index_col=0)

print(df.info())

#df['Date'] = pd.to_datetime(df['Date'],format="%d-%m-%Y")
#print(df.info())

# df['Date'] = pd.to_datetime(df['Date'])

# df['Year'] = df['Date'].dt.year
# df['Month'] = df['Date'].dt.month
# df['Day'] = df['Date'].dt.day


df =pd.read_csv("data_02/patient_data_dates.csv")

df = pd.read_csv("data_02/patient_data_dates.csv", index_col=0)
df.drop(index=26, inplace=True)
# # Allows you to see all rows
pd.set_option('display.max_rows',None)
df['Date'] = pd.to_datetime(df['Date'])

# print(df)

avg_cal = df["Calories"].mean()
df["Calories"].fillna(avg_cal, inplace=True)



"""
Best practices
"""

df.dropna(inplace = True)
df = df.reset_index(drop=True)
df.loc[7,'Duration'] = 45
# df.at[7, 'Duration'] = 45
# df['Duration'] = df['Duration'] .replace([450], 45)
print(df)

df = pd.read_csv("data_02/iris.csv")

col_names =df.columns.tolist()
print(col_names)

df["sepal_length_sq"] = df["sepal_length"].apply(lambda x: x**2)

# aggregation
grouped = df.groupby('class')
mean_square_values = grouped['sepal_length_sq'].mean()
sum_squared_values = grouped['sepal_length_sq'].sum()
count_squared_values = grouped['sepal_length_sq'].count()

# Append & Merge
df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")

df = pd.concat([df1,df2], ignore_index=True)

df1 = pd.read_csv('data_02/person_education.csv',index_col=0)
df2 = pd.read_csv('data_02/person_work.csv',index_col=0)
## inner join
df_merge = pd.merge(df1,df2,on='id')
## outer join
df_merge2 = pd.merge(df1, df2, on='id', how='outer')

df.to_csv("data_02/iris_data_cleaned.csv")




