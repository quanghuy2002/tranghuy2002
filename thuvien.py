import pandas as pd

dataframe_ex = {"a":[1, 3, 5, 7, 9], "b":[-2, 4, 6, 8, 22], "c":[23, 45, 44, 54, 64]}
df= pd.DataFrame(dataframe_ex)
print(df)
print('In ra cot dau cua 1 data frame')
print(df['a'])
print('In ra hang dau tien cua 1 data frame')
print(df.loc[0])
print('In ra phan tu dau cua 1 series')
series_data = pd.Series([1, 3, 5, 7, 9])
print(series_data[1])