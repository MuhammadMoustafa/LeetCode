1class Solution:
2    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
3        tower = [[0] * (r + 1) for r in range(query_row + 1)]
4
5        tower[0][0] = poured
6
7        for r in range(query_row):
8            for c in range(len(tower[r])):
9                overflow = (tower[r][c] - 1) / 2
10                if overflow > 0:
11                    tower[r+1][c] += overflow
12                    tower[r+1][c+1] += overflow 
13
14        return min(1, tower[query_row][query_glass])
15                