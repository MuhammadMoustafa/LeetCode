1class Solution:
2    def minFlips(self, s: str) -> int:
3        n = len(s)
4        # Concatenate string to handle cyclic shifts (Type-1)
5        s = s + s
6        
7        res = float("inf")
8        diff1 = 0
9        l = 0
10        
11        for r in range(len(s)):
12            # If current char doesn't match target, increment diff
13            if s[r] != str(r % 2):
14                diff1 += 1
15            
16            # When window size is greater than n, shrink from left
17            if (r - l + 1) > n:
18                if s[l] != str(l % 2):
19                    diff1 -= 1
20                l += 1
21            
22            # When window is exactly size n, check results
23            if (r - l + 1) == n:
24                res = min(res, diff1, n-diff1)
25                
26        return res