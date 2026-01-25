1class Solution:
2    def minimumDifference(self, nums: List[int], k: int) -> int:
3        if k == 1:
4            return 0
5            
6        n = len(nums)
7        nums = sorted(nums)
8        result = float('inf')
9
10        for i in range(n-k+1):
11            diff = nums[i+k-1]  - nums[i]
12            result = min(result, diff)
13
14        return result
15
16            