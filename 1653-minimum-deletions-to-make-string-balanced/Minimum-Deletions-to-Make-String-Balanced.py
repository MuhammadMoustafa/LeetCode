1class Solution:
2    def minimumDeletions(self, s: str) -> int:
3        n = len(s)
4        b_before = [0] * n
5        a_after = [0] * n
6        for i in range(1, n):
7            is_b = 1 if s[i-1] == 'b' else 0
8            b_before[i] = b_before[i-1] + is_b
9
10        for i in range(n-2, -1, -1):
11            is_a = 1 if s[i+1] == 'a' else 0
12            a_after[i] = a_after[i+1] + is_a
13
14        result = float('inf')
15        for i in range(n):
16            result = min(result, a_after[i] + b_before[i])
17
18        return result