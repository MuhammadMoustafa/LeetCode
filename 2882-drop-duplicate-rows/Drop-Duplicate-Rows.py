1import pandas as pd
2
3def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
4    customers.drop_duplicates(subset=['email'], keep='first', inplace=True)
5    return customers