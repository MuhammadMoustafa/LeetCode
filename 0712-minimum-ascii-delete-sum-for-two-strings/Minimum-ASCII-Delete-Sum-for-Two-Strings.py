1class Solution:
2    def minimumDeleteSum(self, s1: str, s2: str) -> int:
3        
4        m, n = len(s1), len(s2)
5
6        result = [[0] * (n+1) for _ in range(m+1)]
7        
8        for i in range(1, m+1):
9            result[i][0] = result[i-1][0] + ord(s1[i-1])
10        
11        for j in range(1, n+1):
12            result[0][j] = result[0][j-1] + ord(s2[j-1])
13                
14        for i in range(1, m+1):
15            for j in range(1, n+1):
16
17                if s1[i-1] == s2[j-1]:
18                    result[i][j] = result[i-1][j-1]
19                else:
20                    result[i][j] = min(
21                        result[i-1][j] + ord(s1[i-1]), 
22                        result[i][j-1] + ord(s2[j-1]),
23                        )
24
25        return result[m][n]