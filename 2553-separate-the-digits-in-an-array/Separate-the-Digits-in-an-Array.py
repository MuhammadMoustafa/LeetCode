1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        digit_list = []
4        for num in nums:
5            if num > 9:
6                for d in str(num):
7                    digit_list.append(int(d))
8            else:
9                digit_list.append(num)
10        return digit_list