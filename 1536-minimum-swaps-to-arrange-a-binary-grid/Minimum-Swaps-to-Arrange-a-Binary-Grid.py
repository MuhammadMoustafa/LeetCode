1class Solution:
2    def minSwaps(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        trailing_zeros = []
5        
6        # 1. Count trailing zeros for each row correctly
7        for row in grid:
8            count = 0
9            for val in reversed(row):
10                if val == 0:
11                    count += 1
12                else:
13                    break
14            trailing_zeros.append(count)
15            
16        total_swaps = 0
17        
18        for i in range(n):
19            needed = n-1-i
20            found = False
21            for j in range(i, n):
22                if trailing_zeros[j] >= needed:
23                    total_swaps += (j-i)
24                    val = trailing_zeros.pop(j)
25                    trailing_zeros.insert(i, val)
26                    found = True
27                    break
28                
29            if not found:
30                return -1
31            
32        return total_swaps