1class Solution:
2    def maxDistance(self, colors: List[int]) -> int:
3        n = len(colors)
4
5        left = 0
6        while colors[left] == colors[-1]:
7            left += 1
8
9        right = n-1
10        while colors[right] == colors[0]:
11            right -= 1
12
13        return max(n-1-left, right) 