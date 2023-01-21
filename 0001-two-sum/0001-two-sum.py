class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for idx, val in enumerate(nums):
            com = target - val
            if com in h:
                return [h[com], idx]
            else:
                h[val] = idx
                 