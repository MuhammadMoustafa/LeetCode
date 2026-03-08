1class Solution:
2    def findDifferentBinaryString(self, nums: List[str]) -> str:
3        l = []
4        n = len(nums)
5        for i in range(n):
6            if nums[i][i] == '0':
7                l.append('1')
8            else:
9                l.append('0')
10        return ''.join(l)