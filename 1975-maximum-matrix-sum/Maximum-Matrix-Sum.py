1class Solution:
2    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
3        
4        row = len(matrix)
5        col = len(matrix[0])
6
7        min_abs_number = 10**6
8        negative_count = 0
9        total = 0
10        for i in range(row):
11            for j in range(col):
12                num = matrix[i][j]
13                abs_num = abs(num)
14
15                if abs_num < min_abs_number:
16                    min_abs_number = abs_num
17
18                if num < 0:
19                    negative_count += 1
20
21                total += abs_num
22
23        if negative_count % 2 == 1:
24            total = total - 2 * min_abs_number
25
26        return total
27                    