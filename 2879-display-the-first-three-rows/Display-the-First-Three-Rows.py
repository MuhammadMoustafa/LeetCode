1import pandas as pd
2
3def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
4    return employees.head(3)