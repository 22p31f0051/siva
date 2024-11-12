Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data={'Name':['Alice','Bob','Charlie','David'],'Age':[25,30,35,28],'City':['New York','Los Angels','Chicago','Houston']}
>>> df=pd.DataFrame(data)
>>> print(df)
      Name  Age        City
0    Alice   25    New York
1      Bob   30  Los Angels
2  Charlie   35     Chicago
3    David   28     Houston
>>> new_column=['Female','Male','Male','Female']
>>> new_column_name='Gender'
>>> insert_index=1
>>> df.insert(insert_index,new_column_name,new_column)
>>> print("\nDataFrame After adding the new Column:")

DataFrame After adding the new Column:
>>> print(df)
      Name  Gender  Age        City
0    Alice  Female   25    New York
1      Bob    Male   30  Los Angels
2  Charlie    Male   35     Chicago
3    David  Female   28     Houston
>>> 