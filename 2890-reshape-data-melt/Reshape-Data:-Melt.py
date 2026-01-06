1import pandas as pd
2
3def meltTable(report: pd.DataFrame) -> pd.DataFrame:
4    result = report.melt(
5        id_vars='product',
6        var_name='quarter',
7        value_name='sales'
8    )
9    return result
10    