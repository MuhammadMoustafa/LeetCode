1class Solution:
2    def checkStrings(self, s1: str, s2: str) -> bool:
3        s1_even = "".join(sorted(s1[::2]))
4        s1_odd = "".join(sorted(s1[1::2]))
5
6        s2_even = "".join(sorted(s2[::2]))
7        s2_odd = "".join(sorted(s2[1::2]))
8        
9        return s1_even == s2_even and s1_odd == s2_odd