Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data={'EmployeeID':[101,102,103,104,105],'Name':['Alice','Bob','Charlie','David','Eve'],'Age':[28,32,29,35,26]}
>>> df=pd.DataFrame(data)
>>> print("Initial DataFrame")
Initial DataFrame
>>> print(df)
   EmployeeID     Name  Age
0         101    Alice   28
1         102      Bob   32
2         103  Charlie   29
3         104    David   35
4         105      Eve   26
>>> employee_to_delete='Charlie'
>>> df=df.loc[df['Name']!=employee_to_delete]
>>> print("\nDataFrame after deleting the row for 'Charlie'.")

DataFrame after deleting the row for 'Charlie'.
>>> print(df)
   EmployeeID   Name  Age
0         101  Alice   28
1         102    Bob   32
3         104  David   35
4         105    Eve   26
>>> 