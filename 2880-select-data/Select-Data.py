1import pandas as pd
2
3def selectData(students: pd.DataFrame) -> pd.DataFrame:
4    return students.loc[students["student_id"] == 101, ["name", "age"]]
5    