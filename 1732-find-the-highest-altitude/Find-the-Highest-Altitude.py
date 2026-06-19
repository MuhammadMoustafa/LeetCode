1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        result = 0
4        current_sum = 0
5        for num in gain:
6            current_sum += num
7            result = max(result, current_sum)
8        return result