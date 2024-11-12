Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data={'Name':['Alice','Bob','Charlie','David'],'Age':[25,30,35,28],'City':['New York','Los Angels','Chicago','Houston']}
>>> df=pd.DataFrame(data)
>>> print("Initial Data Frame")
Initial Data Frame
>>> print(df)
      Name  Age        City
0    Alice   25    New York
1      Bob   30  Los Angels
2  Charlie   35     Chicago
3    David   28     Houston
>>> new_columns={'Gender':['Female','Male','Male','Female'],'Grade':['A','B','C','B']}
>>> df['Gender']=new_columns['Gender']
>>> df['Grade']=new_columns['Grade']
>>> print("DataFrame after adding a new columns: ")
DataFrame after adding a new columns: 
>>> print(df)
      Name  Age        City  Gender Grade
0    Alice   25    New York  Female     A
1      Bob   30  Los Angels    Male     B
2  Charlie   35     Chicago    Male     C
3    David   28     Houston  Female     B
>>> 