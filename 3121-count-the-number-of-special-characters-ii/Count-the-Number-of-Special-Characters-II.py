1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        last_low = {}
4        first_up = {}
5        for i, c in enumerate(word):
6            if c.islower():
7                last_low[c] = i
8            else:
9                if c not in first_up:
10                    first_up[c] = i
11        ans = 0
12        for c in string.ascii_lowercase:
13            if (
14                c in last_low
15                and c.upper() in first_up
16                and last_low[c] < first_up[c.upper()]
17            ):
18                ans += 1
19        return ans