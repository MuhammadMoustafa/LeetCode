1class Solution:
2    def minMirrorPairDistance(self, nums: List[int]) -> int:
3
4        last_seen_reversed = {}
5        min_dist = float('inf')
6
7        for j in range(len(nums)):
8            current_val = nums[j]
9            if current_val in last_seen_reversed:
10                i = last_seen_reversed[current_val]
11                min_dist = min(min_dist, j - i)
12            
13            target = int(str(current_val)[::-1])
14            last_seen_reversed[target] = j
15
16        return min_dist if min_dist != float('inf') else -1
17