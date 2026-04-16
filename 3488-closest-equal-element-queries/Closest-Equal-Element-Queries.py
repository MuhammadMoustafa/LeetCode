1import bisect
2
3class Solution:
4    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
5        n = len(nums)
6        # Dictionary mapping value -> list of indices where it appears
7        val_to_indices = {}
8        for i, v in enumerate(nums):
9            val_to_indices.setdefault(v, []).append(i)
10        
11        res = []
12        for q_idx in queries:
13            target_val = nums[q_idx]
14            indices = val_to_indices[target_val]
15            
16            if len(indices) < 2:
17                res.append(-1)
18                continue
19            
20            # Find where the current query index sits in the sorted list of indices
21            pos = bisect.bisect_left(indices, q_idx)
22            
23            # The closest must be the neighbor to the left or the neighbor to the right
24            # Python's negative indexing (pos-1) handles the left wrap-around perfectly.
25            # Modulo indexing handles the right wrap-around.
26            left_neighbor = indices[pos - 1]
27            right_neighbor = indices[(pos + 1) % len(indices)]
28            
29            # Circular distance formula
30            dist_l = min(abs(q_idx - left_neighbor), n - abs(q_idx - left_neighbor))
31            dist_r = min(abs(q_idx - right_neighbor), n - abs(q_idx - right_neighbor))
32            
33            res.append(min(dist_l, dist_r))
34            
35        return res