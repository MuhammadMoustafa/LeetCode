1class Solution:
2    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        count = 0
5
6        pref = [ [0]* cols for _ in range(rows) ]
7        is_x = [ [False]* cols for _ in range(rows) ]
8
9        xmap = {
10            'X': 1,
11            'Y': -1,
12            '.': 0
13        }
14
15        for r in range(rows):
16            for c in range(cols):
17
18                top = pref[r-1][c] if r > 0 else 0
19                left = pref[r][c-1] if c > 0 else 0
20                top_left = pref[r-1][c-1] if (r > 0 and c > 0) else 0
21
22                top_x = is_x[r-1][c] if r > 0 else False
23                left_x = is_x[r][c-1] if c > 0 else False
24                top_left_x = is_x[r-1][c-1] if (r > 0 and c > 0) else False
25
26                
27                pref[r][c] = xmap[grid[r][c]] + top + left - top_left
28                is_x[r][c] = grid[r][c] == 'X' or top_x or left_x or top_left_x
29                
30                if is_x[r][c] and pref[r][c] == 0:
31                    count += 1
32
33        return count