1import pandas as pd
2
3def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
4    result = pd.concat([df1, df2])
5    return result