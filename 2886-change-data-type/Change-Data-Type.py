1import pandas as pd
2
3def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
4    students['grade'] = students['grade'].astype(int)
5    return students