1class Solution:
2    def findKthBit(self, n: int, k: int) -> str:
3        def reverse_bits(s):
4            s = list(s)
5            for i in range(len(s)):
6                s[i] = '1' if s[i] == '0' else '0'
7            return ''.join(s)
8        
9        s = '0'
10        for _ in range(1, n):
11            s = s + '1' + reverse_bits(s)[::-1]
12
13        return s[k-1]