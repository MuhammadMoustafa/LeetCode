1class Solution:
2    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
3        MOD = 10**9 + 7
4        for l, r, k, v in queries:
5            for i in range(l, r+1, k):
6                nums[i] = (nums[i] * v) % MOD
7
8        result = 0
9        for num in nums:
10            result ^= num
11        
12        return result