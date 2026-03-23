1class Solution:
2    def maxProductPath(self, grid: List[List[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4        dp = [ [(None, None)]*(n) for _ in range(m) ]
5        MOD = 10**9 + 7
6        
7        for i in range(m):
8            for j in range(n):
9                if grid[i][j] == 0:
10                    dp[i][j] = (0, 0)
11                    continue
12                if i == 0 and j == 0:
13                    dp[i][j] = (grid[i][j], grid[i][j])
14                    continue
15                if i == 0:
16                    dp[i][j] = (dp[i][j-1][0]*grid[i][j], dp[i][j-1][0]*grid[i][j])
17                    continue
18                if j == 0:
19                    dp[i][j] = (dp[i-1][j][0]*grid[i][j], dp[i-1][j][0]*grid[i][j])
20                    continue
21
22                possible_outcoems = [
23                    grid[i][j] * dp[i-1][j][0],
24                    grid[i][j] * dp[i-1][j][1], 
25                    grid[i][j] * dp[i][j-1][0],
26                    grid[i][j] * dp[i][j-1][1],
27                ]
28                dp[i][j] = (min(possible_outcoems), max(possible_outcoems))
29
30        return dp[m-1][n-1][1] % MOD if dp[m-1][n-1][1] >= 0 else -1