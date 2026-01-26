1class Solution:
2    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
3        arr = sorted(arr)
4        min_diff = float('inf')
5        result = []
6        for a, b in pairwise(arr):
7            diff = b - a
8            
9            if diff > min_diff:
10                continue
11            
12            if diff < min_diff:
13                min_diff = diff 
14                result = []
15
16            result.append((a, b))
17        
18        return result
19
20