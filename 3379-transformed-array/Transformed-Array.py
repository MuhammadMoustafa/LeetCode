1class Solution:
2    def constructTransformedArray(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        result = [nums[ (idx + val) % n ] for idx, val in enumerate(nums) ]
5
6        return result