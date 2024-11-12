Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],'Age': [25, 30, 35, 28],'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
>>> df = pd.DataFrame(data)
>>> print(df)
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   28      Houston
>>> new_row=pd.DataFrame([{'Name':'Eve','Age':24,'City':'San Fransisco'}])
>>> df=pd.concat([df,new_row],ignore_index=True)
>>> print("\nDataFrame After Adding a new row:")

DataFrame After Adding a new row:
>>> print(df)
      Name  Age           City
0    Alice   25       New York
1      Bob   30    Los Angeles
2  Charlie   35        Chicago
3    David   28        Houston
4      Eve   24  San Fransisco
>>> 