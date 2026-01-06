1import pandas as pd
2
3def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
4    return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]   