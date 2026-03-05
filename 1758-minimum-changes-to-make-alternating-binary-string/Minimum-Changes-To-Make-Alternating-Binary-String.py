1class Solution:
2    def minOperations(self, s: str) -> int:
3        n = len(s)
4        s1 = "0"
5        s2 = "1"
6
7        def toggle_char(c):
8            return '0' if c == '1' else '1'
9
10        for _ in range(1, n):
11            s1 += toggle_char(s1[-1])
12            s2 += toggle_char(s2[-1])
13
14        r1 = 0
15        r2 = 0
16
17        for i in range(n):
18            if s[i] != s1[i]:
19                r1 += 1
20            if s[i] != s2[i]:
21                r2 += 1
22
23        return min(r1, r2)
24