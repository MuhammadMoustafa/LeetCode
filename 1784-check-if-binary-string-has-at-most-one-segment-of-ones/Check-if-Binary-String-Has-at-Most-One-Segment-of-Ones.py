1from itertools import pairwise
2
3class Solution:
4    def checkOnesSegment(self, s: str) -> bool:
5        found_zero = False
6        for l in s:
7            if l == '0':
8                found_zero = True
9            if found_zero and l == '1':
10                return False
11
12        return True