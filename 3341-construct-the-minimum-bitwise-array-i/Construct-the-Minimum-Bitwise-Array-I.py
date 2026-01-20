1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3
4        ans = []
5
6        for num in nums:
7            if num == 2:
8                ans.append(-1)
9                continue
10
11            temp = num
12            pos = 0
13            while (temp & 1):
14                temp >>=1
15                pos += 1
16
17            ans.append( num ^ (1 << (pos-1)) )
18
19        return ans
20        