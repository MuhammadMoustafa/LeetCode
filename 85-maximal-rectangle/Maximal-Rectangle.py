1class Solution:
2    def maximalRectangle(self, matrix: List[List[str]]) -> int:
3        rows = len(matrix)
4        cols = len(matrix[0])
5
6
7        result_rows = [ [0] * (cols) for _ in range(rows)]
8        result = [ [0] * (cols) for _ in range(rows)]
9
10        for row in range(rows):
11            for col in range(cols):
12                if row == 0 and col == 0:
13                    result_rows[row][col] = 1 if matrix[row][col] == '1' else 0
14                    result[row][col] = result_rows[row][col]
15                    continue
16
17                if matrix[row][col] == '1':
18                    result_rows[row][col] = result_rows[row][col-1] + 1
19
20                    current_min_width = result_rows[row][col]
21                    best_area = 0
22                    for k in range(row, -1, -1):
23                        height = row - k + 1
24                        current_min_width = min(current_min_width, result_rows[k][col])
25                        best_area = max(best_area, height*current_min_width)
26
27
28                    result[row][col] = max(
29                        result_rows[row][col], 
30                        best_area
31                        )
32
33                else:
34                    result_rows[row][col] = 0
35                        
36        print(result_rows, "\n\n")
37        print(result, "\n\n")
38        
39        return max([max(row) for row in result])