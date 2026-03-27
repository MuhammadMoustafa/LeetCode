1class Solution:
2    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
3        rows, cols = len(mat), len(mat[0])
4        rotations = k % cols
5        result = [ [] for _ in range(rows) ]
6        # print("rotations = ", rotations)
7        if rotations == 0:
8            return True
9            
10        for i in range(rows):
11            if i % 2 == 0:
12                ## shift_left
13                result[i] = mat[i][rotations:] + mat[i][:rotations]
14            else:
15                ## shift_right
16                result[i] = mat[i][-rotations:] + mat[i][:-rotations]
17
18        return result == mat