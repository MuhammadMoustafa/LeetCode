1class Solution:
2    def numSpecial(self, mat: List[List[int]]) -> int:
3
4        def get_col_sum(col_index):
5            return sum([row[col_index] for row in mat])
6
7        result = 0
8        for row in mat:
9            if sum(row) == 1:
10                col_index = row.index(1)
11                result += get_col_sum(col_index) == 1
12
13        return result