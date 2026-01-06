1import pandas as pd
2
3def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
4    return students.dropna(subset=['name'])