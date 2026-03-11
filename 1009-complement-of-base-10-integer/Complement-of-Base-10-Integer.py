1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3        bin_n = format(n, "b")
4        comp = []
5        for i in bin_n:
6            if i == '0':
7                comp.append('1')
8            else:
9                comp.append('0')
10
11        return int("".join(comp), 2)