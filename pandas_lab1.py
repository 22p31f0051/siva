Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> students=['Alice','Bob','Charlie','David','Eve','Frank','Grace','Hunnah','Ivy','Jack']
>>> exam_scores=[92,88,76,94,82,90,86,89,78,91]
>>> exam_scores_series=pd.series(data=exam_scores, index=students)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    exam_scores_series=pd.series(data=exam_scores, index=students)
AttributeError: module 'pandas' has no attribute 'series'
>>> exam_scores_series=pd.Series(data=exam_scores, index=students)
>>> print(exam_scores_series)
Alice      92
Bob        88
Charlie    76
David      94
Eve        82
Frank      90
Grace      86
Hunnah     89
Ivy        78
Jack       91
dtype: int64
>>> exam_scores_series=pd.Series(data=exam_scores, index=students, name="Exam scores")
>>> print(exam_scores_series)
Alice      92
Bob        88
Charlie    76
David      94
Eve        82
Frank      90
Grace      86
Hunnah     89
Ivy        78
Jack       91
Name: Exam scores, dtype: int64
>>> 