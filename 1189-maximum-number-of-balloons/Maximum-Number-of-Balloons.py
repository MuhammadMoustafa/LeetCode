1from collections import Counter
2
3class Solution:
4    def maxNumberOfBalloons(self, text: str) -> int:
5        f = Counter(text)
6
7        return min([
8            f['b'],
9            f['a'],
10            f['l'] >> 1, # multiply by 2
11            f['o'] >> 1,
12            f['n']
13        ])