Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
da
>>> data={'OrderID':[101,102,103,104,105],'Product':['Widget','Gadjet','Widget','Doodad','Widget'],'Quantity':[10,5,0,7,15],'Status':['Shipped','Canceled','Canceled','Shipped','Shipped']}
>>> df=pd.DataFrame(data)
>>> print("Initial DataFrame")
Initial DataFrame
>>> print(df)
   OrderID Product  Quantity    Status
0      101  Widget        10   Shipped
1      102  Gadjet         5  Canceled
2      103  Widget         0  Canceled
3      104  Doodad         7   Shipped
4      105  Widget        15   Shipped
>>> df=df[df['Status']!='Cancelled']
>>> print("DataFrame after deleting 'Canceled' orders")
DataFrame after deleting 'Canceled' orders
>>> print(df)
   OrderID Product  Quantity    Status
0      101  Widget        10   Shipped
1      102  Gadjet         5  Canceled
2      103  Widget         0  Canceled
3      104  Doodad         7   Shipped
4      105  Widget        15   Shipped
>>> df=df[df['Status']!='Cancelled']
>>> print(df)
   OrderID Product  Quantity    Status
0      101  Widget        10   Shipped
1      102  Gadjet         5  Canceled
2      103  Widget         0  Canceled
3      104  Doodad         7   Shipped
4      105  Widget        15   Shipped
>>> df=df[df['Status']!='Canceled']
>>> print(df)
   OrderID Product  Quantity   Status
0      101  Widget        10  Shipped
3      104  Doodad         7  Shipped
4      105  Widget        15  Shipped
>>> 