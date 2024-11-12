Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data={'EmployeeID':[101,102,103,104,105],'Name':['Alice','Bob','Charlie','David','Eve'],'Age':[28,32,29,35,26],'Photo':['C:/Users/Siva/OneDrive/Pictures/2.png','C:/Users/Siva/OneDrive/Pictures/3.png','C:/Users/Siva/OneDrive/Pictures/computer-img.png','C:/Users/Siva/OneDrive/Pictures/laptop-img.png','C:/Users/Siva/OneDrive/Pictures/mobile-img.png']}
>>> df=pd.DataFrame(data)
>>> print("Initial DataFrame")
Initial DataFrame
>>> print(df)
   EmployeeID     Name  Age                                             Photo
0         101    Alice   28             C:/Users/Siva/OneDrive/Pictures/2.png
1         102      Bob   32             C:/Users/Siva/OneDrive/Pictures/3.png
2         103  Charlie   29  C:/Users/Siva/OneDrive/Pictures/computer-img.png
3         104    David   35    C:/Users/Siva/OneDrive/Pictures/laptop-img.png
4         105      Eve   26    C:/Users/Siva/OneDrive/Pictures/mobile-img.png
>>> df=df.drop('Photo',axis=1)
>>> print('\nDataFrame after deleting the 'Photo' column:")
      
SyntaxError: invalid syntax
>>> print('\nDataFrame after deleting the Photo column:")
      
SyntaxError: EOL while scanning string literal
>>> print("\nDataFrame after deleting the 'Photo' column.")

DataFrame after deleting the 'Photo' column.
>>> print(df)
   EmployeeID     Name  Age
0         101    Alice   28
1         102      Bob   32
2         103  Charlie   29
3         104    David   35
4         105      Eve   26
>>> 