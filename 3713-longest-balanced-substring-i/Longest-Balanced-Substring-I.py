1class Solution:
2    def longestBalanced(self, s: str) -> int:
3        n = len(s)
4        result = 0
5        for i in range(0, n):
6            letter_map = {}
7            for j in range(i, n):
8                l = s[j]
9                if s[j] in letter_map:
10                    letter_map[l] += 1
11                else:
12                    letter_map[l] = 1
13
14                val_list = list(letter_map.values())
15
16                if len(val_list) >= 1:
17                    length = val_list[0]
18                
19                is_balanced = True
20                for k in range(1, len(val_list)):
21                    if val_list[k] != val_list[k-1]:
22                        is_balanced = False
23                        break
24                    else:
25                        length += val_list[k]
26                
27                if val_list and is_balanced:
28                    result = max(result, length)
29
30        return result