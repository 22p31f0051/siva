Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>>  data={'Name':['Alice','Bob','Charlie','David'],'Age':[25,30,35,28],'City':['New York','Los Angels','Chicago','Houston']}
 
SyntaxError: unexpected indent
>>> data={'Name':['Alice','Bob','Charlie','David'],'Age':[25,30,35,28],'City':['New York','Los Angels','Chicago','Houston']}
>>> df=pd.DataFrame(data)
>>> print("Initial DataFrame: ")
Initial DataFrame: 
>>> print(df)
      Name  Age        City
0    Alice   25    New York
1      Bob   30  Los Angels
2  Charlie   35     Chicago
3    David   28     Houston
>>>  new_row=pd.DataFrame{'Name':'Eve','Age':24,'City':'San Fransisco'}
 
SyntaxError: unexpected indent
>>> new_row=pd.DataFrame{'Name':'Eve','Age':24,'City':'San Fransisco'}
SyntaxError: invalid syntax
>>> new_row={'Name':'Eve','Age':24,'City':'San Fransisco'}
>>> insert_index=1.5
>>> df.loc[insert_index]=new_row
>>> df=df.sort_index().reset_index(drop=True)
>>> print("\nDataFrame Adding new rows.")

DataFrame Adding new rows.
>>> print(df)
      Name  Age           City
0    Alice   25       New York
1      Bob   30     Los Angels
2      Eve   24  San Fransisco
3  Charlie   35        Chicago
4    David   28        Houston
>>> 