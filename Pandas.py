from termios import VWERASE
import pandas as pd
import os

# Files to load
cwd = os.getcwd()
print(cwd)
# student_data_to_load = os.path.join(cwd, "students_complete.csv")
student_data_to_load='/Users/vsingh/Documents/UCSD/GIT/School_District_Analysis/Resources/missing_grades.csv'
student_data_df = pd.read_csv(student_data_to_load)

student_data_df
student_data_df_vs  = student_data_df["student_name"]
print(student_data_df_vs)
# print(student_data_df["student_name"])
