1class Solution:
2    def separateSquares(self, squares: List[List[int]]) -> float:
3        
4        def get_total_area(squares):
5            total = 0
6            for square in squares:
7                total += square[2]**2
8            return total
9        
10        def get_area_below_line(squares, line_y):
11            area = 0
12            for square in squares:
13                square_bottom = square[1]
14                square_top = square[1] + square[2]
15
16                if square_top <= line_y:
17                    area += square[2]**2
18                elif square_bottom < line_y < square_top:
19                    height_below = line_y - square_bottom
20                    area += height_below * square[2]
21            return area
22        
23        total_area = get_total_area(squares)
24        target_area = total_area / 2
25
26
27        lower_bound = min(square[1] for square in squares)
28        upper_bound = max(square[1] + square[2] for square in squares)
29
30        mid_line = (lower_bound + upper_bound) / 2
31        current_area = get_area_below_line(squares, mid_line)
32
33        while upper_bound - lower_bound > 1e-5:
34            if current_area < target_area:
35                lower_bound = mid_line
36            else:
37                upper_bound = mid_line        
38            mid_line = (lower_bound + upper_bound) / 2
39            current_area = get_area_below_line(squares, mid_line)
40        return mid_line
41        