1class Solution:
2    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
3        hSorted = sorted(hBars)
4        vSorted = sorted(vBars)
5
6        def get_longest_seq(lst):
7            longest_seq = 0
8            longest_start = 0
9            
10            current_seq = 1
11            current_start = lst[0]
12
13            for idx, val in enumerate(lst[1:], start=1):
14                if val == lst[idx-1] + 1:
15                    current_seq += 1
16
17                else:
18                    if current_seq > longest_seq:
19                        longest_seq = current_seq
20                        longest_start = current_start
21
22                    current_start = lst[idx]
23                    current_seq = 1
24
25            return max(longest_seq, current_seq)
26
27        hLen = get_longest_seq(hSorted)+1 
28        vLen = get_longest_seq(vSorted)+1
29        
30        min_length = min(hLen, vLen)
31        return min_length ** 2
32        