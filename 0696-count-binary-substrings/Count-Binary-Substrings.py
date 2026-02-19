1class Solution:
2    def countBinarySubstrings(self, s: str) -> int:
3        n = len(s)
4        prev = 0
5        curr = 1
6        ans = 0
7        
8        for i in range(1, n):
9            if s[i] == s[i - 1]:
10                curr += 1
11            else:
12                ans += min(prev, curr)
13                prev = curr
14                curr = 1
15        
16        ans += min(prev, curr)
17        return ans
18
19    # def countBinarySubstrings(self, s: str) -> int:
20        
21    #     def sub_func(s, target, anti_target):    
22    #         con_target = 0
23    #         con_anti = 0
24    #         result = 0
25
26    #         i = 0
27    #         n = len(s)
28
29    #         while i < n:
30    #             if s[i] == target:
31    #                 con_target += 1
32    #             else:
33    #                 while i < n and s[i] == anti_target and con_anti < con_target:
34    #                     con_anti +=1
35    #                     i += 1
36    #                 result += con_anti
37    #                 con_anti = 0
38    #                 con_target = 1 if i < n and s[i] == target else 0
39    #             i += 1
40
41    #         return result
42        
43    #     result = sub_func(s, "0", "1") + sub_func(s, "1", "0")
44    #     return result