Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> categories=['Groceries','Utilities','Rent','Transportation','Entertainment']
>>> expenses=[500,200,1200,300,150]
>>> expenses_series=pd.Series(data=expenses, index=categories, name="Monthly Expenses")
>>> print(expenses_series)
Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
Name: Monthly Expenses, dtype: int64
>>> 