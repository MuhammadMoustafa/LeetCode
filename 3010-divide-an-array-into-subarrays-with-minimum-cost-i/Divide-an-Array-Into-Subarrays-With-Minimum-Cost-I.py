1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        sorted_nums = sorted(nums)
4        starts = sorted_nums[0:2]
5        if nums[0] in starts:
6            starts.append(sorted_nums[2])
7        else:
8            starts.append(nums[0])
9
10        return sum(starts)