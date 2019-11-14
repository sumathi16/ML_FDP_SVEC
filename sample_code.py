import numpy as np
import pandas as pd
path = 'https://raw.githubusercontent.com/sumathi16/ML_FDP_SVEC/master/'
fileName1 = 'student_marks.csv'
fileName2 = 'student_data.csv'
student_marks_df = pd.read_csv(path+fileName1)
student_data_df = pd.read_csv(path+fileName2)
num_cols = student_marks_df.columns[student_marks_df.dtypes != object]
for col in num_cols:
    m = student_marks_df[col].mean()
    student_marks_df[col] = student_marks_df[col].fillna(m)    