1class Solution:
2    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
3        n, m = len(grid), len(grid[0])
4        MOD = 12345
5        res = [[0] * m for _ in range(n)]
6        
7        # Pass 1: Suffix Products
8        running_prod = 1
9        for r in range(n - 1, -1, -1):
10            for c in range(m - 1, -1, -1):
11                res[r][c] = running_prod
12                running_prod = (running_prod * grid[r][c]) % MOD
13                
14        # Pass 2: Prefix Products
15        running_prod = 1
16        for r in range(n):
17            for c in range(m):
18                res[r][c] = (res[r][c] * running_prod) % MOD
19                running_prod = (running_prod * grid[r][c]) % MOD
20                
21        return res