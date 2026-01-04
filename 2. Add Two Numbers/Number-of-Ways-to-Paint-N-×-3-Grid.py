1class Solution:
2    def numOfWays(self, n: int) -> int:
3
4        ABA = 6
5        ABC = 6
6        MOD = 10**9 + 7
7
8        for row in range (n-1):
9            
10            new_ABA = (3*ABA + 2*ABC) % MOD
11            new_ABC = (2*ABA + 2*ABC) % MOD
12
13            ABA = new_ABA
14            ABC = new_ABC
15
16        return (ABA + ABC) % MOD
17