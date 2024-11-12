Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
mon
>>> months=['Januarey','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
>>> sales_data=[12000,13500,14200,12800,14000,15500,16200,15800,16500,17800,18500,17200]
>>> sales_series=pd.Series(sales_data,index=months,name='Monthly Sales(USD)')
>>> print(sales_series)
Januarey    12000
Feb         13500
Mar         14200
Apr         12800
May         14000
Jun         15500
Jul         16200
Aug         15800
Sep         16500
Oct         17800
Nov         18500
Dec         17200
Name: Monthly Sales(USD), dtype: int64
>>> 