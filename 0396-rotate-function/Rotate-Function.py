1class Solution:
2    def maxRotateFunction(self, nums: List[int]) -> int:
3        f, n, total = 0, len(nums), sum(nums)
4        for i, num in enumerate(nums):
5            f += i*num
6        res = f
7        for i in range(n-1, 0, -1):
8            f = f + total - n * nums[i]
9            res = max(res, f)
10
11        return res     