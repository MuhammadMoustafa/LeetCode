1class Solution:
2    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
3        
4
5        def get_possible_lengths(lst, boundary):
6            lst = sorted(lst + [1, boundary])
7            current_seq = 0
8
9            result = set()
10
11            return {
12                lst[j] - lst[i]
13                for i in range(len(lst))
14                for j in range(i + 1, len(lst))
15            }
16
17        h_seq = get_possible_lengths(hFences, m)
18        v_seq = get_possible_lengths(vFences, n)
19        
20        intersection = h_seq & v_seq
21
22        if not intersection:
23            return -1
24
25        max_length = max(intersection)
26        return (max_length ** 2) % (10**9 + 7)