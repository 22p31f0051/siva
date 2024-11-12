Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
d
>>> data={'Name':['Alice','Bob','Charlie','David'],'Age':[:25,30,35,28],'City':['New York','Los Angels','Chicago','Houston']}
SyntaxError: invalid syntax
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
>>> new_rows=pd.DataFrame([{'Name':'Eve','Age':24,'City':'San Fransisco'},{'Name':'Frank','Age':32,'City':'Miami'},{'Name':'Grace','Age':29,'City':'Seattle'}])
>>> df=pd.concat([df,new_rows],ignore_index=True)
>>> print("\nDataFrame Adding new rows.")

DataFrame Adding new rows.
>>> print(df)
      Name  Age           City
0    Alice   25       New York
1      Bob   30     Los Angels
2  Charlie   35        Chicago
3    David   28        Houston
4      Eve   24  San Fransisco
5    Frank   32          Miami
6    Grace   29        Seattle
>>> 