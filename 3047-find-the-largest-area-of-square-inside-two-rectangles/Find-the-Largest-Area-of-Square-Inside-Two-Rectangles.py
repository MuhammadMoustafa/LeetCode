1class Solution:
2    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
3        
4        max_length = 0
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
24            x1, x2, y1, y2 = squares[i]
25            if min(x2-x1, y2-y1) <= max_length:
26                continue
27
28            for j in range(i+1, len(squares)):
29                x3, x4, y3, y4 = squares[j]
30                if min(x4-x3, y4-y3) <= max_length <= max_length:
31                    continue
32
33                sx1, sx2 = max(x1, x3), min(x2, x4)
34                sy1, sy2 = max(y1, y3), min(y2, y4)
35
36                if sx2 < sx1:
37                    break
38                if sy2 < sy1:
39                    continue
40     
41                current_length = min(sx2-sx1, sy2-sy1)
42                if current_length > max_length:
43                    max_length = current_length
44
45        return max_length ** 2
46