1import pandas as pd
2
3def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
4    weather = weather.pivot(
5        index='month',
6        columns='city',
7        values='temperature',
8    )
9    return weather