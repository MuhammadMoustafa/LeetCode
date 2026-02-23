1class Solution:
2    def hasAllCodes(self, s: str, k: int) -> bool:
3        comb = set()
4        all_codes = 1 << k  
5        n = len(s)
6
7        if n - k + 1 < all_codes:
8            return False
9
10        for i in range(n-k+1):
11            comb.add(s[i: i+k])
12
13        return len(comb) == all_codes