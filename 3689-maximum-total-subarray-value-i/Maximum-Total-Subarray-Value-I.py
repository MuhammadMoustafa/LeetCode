1class Solution:
2    def maxTotalValue(self, nums: List[int], k: int) -> int:
3        min_val = 10**9
4        max_val = 0
5        for num in nums:
6            min_val = min(num, min_val)
7            max_val = max(num, max_val)
8        return k * (max_val - min_val)