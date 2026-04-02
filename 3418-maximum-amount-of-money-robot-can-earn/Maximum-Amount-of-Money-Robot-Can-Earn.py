1class Solution:
2    def maximumAmount(self, coins: List[List[int]]) -> int:
3        m, n = len(coins), len(coins[0])
4        dp = [ [[-float('inf')] * 3 for _ in range(n+1)] for _ in range(m+1) ]
5
6        for i in range(m):
7            for j in range(n):
8                val = coins[i][j]
9                for k in range(3):
10                    if i == 0 and j == 0:
11                        dp[i][j][k] = val
12                        if k > 0 and val < 0:
13                            dp[i][j][k] = max(dp[i][j][k], 0)
14                        continue
15
16                    res = -float('inf')
17                    if i > 0: res = max(res, dp[i-1][j][k])
18                    if j > 0: res = max(res, dp[i][j-1][k])
19
20                    dp[i][j][k] = max(dp[i][j][k], res + val)
21
22                    if k > 0 and val < 0:
23                        prev_res = -float('inf')
24                        if i > 0: prev_res = max(prev_res, dp[i-1][j][k-1])
25                        if j > 0: prev_res = max(prev_res, dp[i][j-1][k-1])
26                        dp[i][j][k] = max(dp[i][j][k], prev_res)
27
28        return max(dp[m-1][n-1])