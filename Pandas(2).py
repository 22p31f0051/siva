Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data={'Name':['Alice','Bob','Charlie','David'],'Age':[25,30,35,28]}
>>> df=pd.DataFrame(data)
>>> print("Before adding Column")
Before adding Column
>>> print(df)
      Name  Age
0    Alice   25
1      Bob   30
2  Charlie   35
3    David   28
>>> df['City']=['NewYork','Los Angels','Chicago','Houston']
>>> print("After adding Column')
      
SyntaxError: EOL while scanning string literal
>>> print("After adding Column")
After adding Column
>>> print(df)
      Name  Age        City
0    Alice   25     NewYork
1      Bob   30  Los Angels
2  Charlie   35     Chicago
3    David   28     Houston
>>> 