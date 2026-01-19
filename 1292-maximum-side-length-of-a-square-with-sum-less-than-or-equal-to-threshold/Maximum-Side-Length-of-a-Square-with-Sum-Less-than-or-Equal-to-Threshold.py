1class Solution:
2    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
3        m, n = len(mat), len(mat[0])
4        prefix = [[0] * (n+1) for _ in range(m+1)]
5
6        for i in range(1, m+1):
7            for j in range(1, n+1):
8                prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + mat[i-1][j-1]
9
10        minLen = min(m, n)
11        for k in range(minLen, 0, -1):
12            for i in range(m, k-1, -1):
13                for j in range(n, k-1, -1):
14                    gridSum = prefix[i][j] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k]
15                    if gridSum <= threshold:
16                        return k
17
18        return 0