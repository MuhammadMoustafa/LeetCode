1class Solution:
2    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
3        
4        max_area = 0
5
6        squares = [
7            [
8                *sorted([ 
9                    bottomLeft[i][0], 
10                    topRight[i][0] 
11                ]), 
12                *sorted([
13                    bottomLeft[i][1], 
14                    topRight[i][1]
15                ])
16            ]
17            for i in range(len(bottomLeft))
18        ] 
19
20        squares = sorted(squares, key=lambda x: x[0])
21        print(squares)
22
23        for i in range(len(squares)):
24            for j in range(i+1, len(squares)):
25                x1, x2, y1, y2 = squares[i]
26                x3, x4, y3, y4 = squares[j]
27                sx1, sx2 = max(x1, x3), min(x2, x4)
28                sy1, sy2 = max(y1, y3), min(y2, y4)
29
30                if sx2 < sx1 or sy2 < sy1:
31                    continue
32     
33                current_length = min(sx2-sx1, sy2-sy1)
34
35                shared_area = current_length**2
36                if shared_area > max_area:
37                    max_area = shared_area
38
39        return max_area
40