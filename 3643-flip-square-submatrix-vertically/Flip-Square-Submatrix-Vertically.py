1class Solution:
2    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
3        start = x
4        end = x+k-1
5        iterations = k // 2
6        for r in range(iterations):
7            temp = grid[start+r][y:y+k]
8            grid[start+r][y:y+k] = grid[end-r][y:y+k]
9            grid[end-r][y:y+k] = temp
10
11        return grid