1class Solution:
2    def canBeEqual(self, s1: str, s2: str) -> bool:
3        n = 4
4        for i in range(n):
5            if (s1[i] != s2[i] and s1[i] != s2[i-2]):
6                return False
7
8        return True