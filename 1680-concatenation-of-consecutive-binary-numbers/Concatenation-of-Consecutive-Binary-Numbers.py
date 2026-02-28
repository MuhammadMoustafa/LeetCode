1class Solution:
2    def concatenatedBinary(self, n: int) -> int:
3        MOD = 10**9 + 7
4        result = 0
5        bit_length = 0
6
7        for i in range(1, n+1):
8            
9            if i&(i-1) == 0:
10                bit_length += 1
11
12            result = (result << bit_length | i) % MOD
13
14        return result