1class Solution:
2    def minPairSum(self, nums: List[int]) -> int:
3        n = len(nums)
4        sorted_nums = sorted(nums)
5        result = 0
6        for idx in range(0, n, 2):
7            current_sum = sorted_nums[idx]+sorted_nums[n-idx-1]
8            if current_sum > result:
9                result = current_sum
10
11        return result