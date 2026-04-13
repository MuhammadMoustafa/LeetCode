1class Solution:
2    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
3        result = float('inf')
4        n = len(nums)
5
6        for i in range(start, n):
7            if nums[i] == target:
8                result = min(result, abs(i - start))
9                break
10
11        for i in range(start, -1, -1):
12            if nums[i] == target:
13                result = min(result, abs(i - start))
14                break
15
16        return result