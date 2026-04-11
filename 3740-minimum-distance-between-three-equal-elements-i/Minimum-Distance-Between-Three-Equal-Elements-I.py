1class Solution:
2    def minimumDistance(self, nums: List[int]) -> int:
3        map = {}
4
5        for idx, num in enumerate(nums):
6            if num in map:
7                map[num].append(idx)
8            else:
9                map[num] = [idx]
10
11        
12        result = float('inf')
13        
14        for indices in map.values():
15            n = len(indices)
16            if n < 3:
17                continue
18
19            # Check every triplet of consecutive indices
20            for i in range(n - 2):
21                # Distance formula simplifies to 2 * (last_idx - first_idx)
22                current_dist = 2 * (indices[i+2] - indices[i])
23                if current_dist < result:
24                    result = current_dist
25
26        result = -1 if result == float('inf') else result
27        return result
28
29        