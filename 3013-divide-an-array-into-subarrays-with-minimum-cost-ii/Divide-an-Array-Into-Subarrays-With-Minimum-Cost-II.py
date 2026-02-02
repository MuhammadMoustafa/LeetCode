1from sortedcontainers import SortedList
2
3class Solution:
4    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
5        n = len(nums)
6        window_size = dist+1
7        needed_indices = k-1
8        L = SortedList(nums[1: window_size+1])
9        R = SortedList(L[needed_indices:])
10        L = SortedList(L[:needed_indices])
11        min_cost = sum(L)
12        current_cost = min_cost
13                
14        for i in range(window_size+1, n):
15            to_add = nums[i]
16            to_remove = nums[i - window_size]
17            
18            if to_add == to_remove:
19                continue
20            
21            if to_remove in R:
22                R.remove(to_remove)
23            else:
24                L.remove(to_remove)
25                current_cost -= to_remove
26
27            if to_add < L[-1]:
28                swap = L[-1]
29                L.remove(swap)
30                R.add(swap)
31                L.add(to_add)
32                current_cost = current_cost - swap + to_add
33            else:
34                R.add(to_add)
35
36            while len(L) < needed_indices:
37                swap = R[0]
38                R.remove(swap)
39                L.add(swap)
40                current_cost += swap
41                
42            min_cost = min(min_cost, current_cost)
43
44        return nums[0] + min_cost