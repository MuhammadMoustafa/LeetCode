1class Solution:
2    def minOperations(self, s: str) -> int:
3        n = len(s)
4        diff = 0
5        for i in range(len(s)):
6            if s[i] != ('0' if i % 2 == 0 else '1'):
7                diff += 1
8
9        return min(diff, n-diff)
10