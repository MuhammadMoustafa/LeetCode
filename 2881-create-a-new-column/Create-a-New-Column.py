1import pandas as pd
2
3def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
4    employees['bonus'] = 2*employees['salary']
5    return employees
6    