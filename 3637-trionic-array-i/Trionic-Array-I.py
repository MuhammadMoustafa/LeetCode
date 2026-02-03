1class Solution:
2    def isTrionic(self, nums: List[int]) -> bool:
3        if len(nums) < 4:
4            return False
5
6        if nums[1] <= nums[0]:
7            return False
8
9        state = 0
10        n = len(nums)
11
12        for i in range(2, n):
13            if state == 0:
14                if nums[i] < nums[i-1]:
15                    state = 1
16                elif nums[i] == nums[i-1]:
17                    return False
18            elif state == 1:
19                if nums[i] > nums[i-1]:
20                    state = 2
21                elif nums[i] == nums[i-1]:
22                    return False
23            elif state == 2:
24                if nums[i] <= nums[i-1]:
25                    return False
26
27        return state == 2 and nums[-1] > nums[-2]
28
29
30        