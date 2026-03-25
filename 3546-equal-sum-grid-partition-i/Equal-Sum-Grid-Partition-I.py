1class Solution:
2    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
3        m, n = len(grid), len(grid[0])
4        row_prefix = [ 0 for _ in range(m)]
5        col_prefix = [ 0 for _ in range(n)]
6        total = 0
7        for r in range(m):
8            for c in range(n):
9                row_prefix[r] += grid[r][c]
10                col_prefix[c] += grid[r][c]
11                total += grid[r][c]
12
13        target = total / 2
14
15        row_sum = 0
16        for val in row_prefix:
17            row_sum += val
18            if row_sum == target:
19                return True
20
21        col_sum = 0
22        for val in col_prefix:
23            col_sum += val
24            if col_sum == target:
25                return True
26                
27        return False