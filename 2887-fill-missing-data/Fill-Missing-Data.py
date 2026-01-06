1import pandas as pd
2
3def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
4    products['quantity'].fillna(0, inplace=True)
5    return products