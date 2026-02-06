1class Solution:
2    def minRemoval(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        n = len(nums)
5        right = 0
6        max_keep = 0
7
8        for left in range(n):
9
10            while right < n and nums[right] <= k*nums[left]:
11                right += 1
12
13            max_keep = max(max_keep, right - left)
14
15            if right == n-1:
16                break
17
18        return n - max_keep
19
20