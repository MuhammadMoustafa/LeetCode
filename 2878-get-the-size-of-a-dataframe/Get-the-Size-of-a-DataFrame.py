1import pandas as pd
2
3def getDataframeSize(players: pd.DataFrame) -> List[int]:
4    return list(players.shape)
5    