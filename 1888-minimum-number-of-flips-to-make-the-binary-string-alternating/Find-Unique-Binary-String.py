1class Solution:
2    def findDifferentBinaryString(self, nums: List[str]) -> str:
3        n = len(nums[0])
4        nums = set(nums)
5
6        for i in range(2**n):
7            bin_number = format(i, f"0{n}b")
8            if bin_number not in nums:
9                return bin_number