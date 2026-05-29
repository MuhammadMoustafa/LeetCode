1class Solution:
2    def minElement(self, nums: List[int]) -> int:
3        result = 10e5
4
5        for num in nums:
6            # digit_sum = sum([int(c) for c in str(num)])
7            digit_sum = sum(list(map(int, str(num))))
8            result = min(result, digit_sum)
9
10        return result