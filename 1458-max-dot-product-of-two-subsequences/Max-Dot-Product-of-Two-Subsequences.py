1import numpy as np
2
3class Solution:
4    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
5        
6        rows, cols = len(nums1), len(nums2)
7        result = [[0]*cols for _ in range(rows)]
8
9        for row in range(rows):
10            for col in range(cols):
11                current_prod = nums1[row]*nums2[col]
12                
13                if row == 0 and col == 0:
14                     result[row][col] = current_prod
15                elif row == 0:
16                    result[row][col] = max(
17                        current_prod,
18                        result[row][col-1]
19                    )
20                elif col == 0:
21                    result[row][col] = max(
22                        current_prod,
23                        result[row-1][col]
24                    )
25                else:
26                    result[row][col] = max(
27                        result[row][col-1],
28                        result[row-1][col],
29                        result[row-1][col-1] + current_prod,
30                        current_prod
31                    )
32                
33        return result[rows-1][cols-1]