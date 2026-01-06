1import pandas as pd
2
3def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
4    students.columns = ['student_id', 'first_name', 'last_name', 'age_in_years'] 
5    return students