1class Solution:
2    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
3
4        def rotate(matrix):
5            n = len(matrix)
6            # Transpose
7            for i in range(n):
8                for j in range(i + 1, n):
9                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
10            # Reverse rows
11            for row in matrix:
12                row.reverse()
13
14        for _ in range(3):
15            if mat == target:
16                return True
17            rotate(mat)
18
19        return mat == target