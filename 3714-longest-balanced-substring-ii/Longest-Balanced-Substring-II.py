1class Solution:
2    def longestBalanced(self, s: str) -> int:
3        
4        def solve_case_2_letters(s, letter1, letter2):
5            ans = 0
6            total = 0
7            letter_map = {}
8            letter_map[0] = -1
9            n = len(s)
10            for i in range(n):
11                if s[i] == letter1:
12                    total += 1
13                elif s[i] == letter2:
14                    total -= 1
15                else:
16                    letter_map = {}
17                    letter_map[0] = i
18                    total = 0
19                    continue
20                if total in letter_map:
21                    ans = max(ans, i - letter_map[total])
22                else:
23                    letter_map[total] = i
24            return ans
25        
26        # case 1
27        n = len(s)
28        ans = 1
29        count = 1
30        for i in range(1, n):
31            if s[i] == s[i-1]:
32                count += 1
33            else:
34                ans = max(ans, count)
35                count = 1
36        
37        # case 2
38        a1 = solve_case_2_letters(s, 'a', 'b')
39        a2= solve_case_2_letters(s, 'a', 'c')
40        a3= solve_case_2_letters(s, 'b', 'c')
41        
42        ans = max(ans, count, a1, a2, a3)
43
44        # case 3 
45        count = [0, 0, 0]
46        diff_map = {}
47        diff_map[(0, 0)] = -1
48        for i in range(n):
49            count[ord(s[i]) - ord('a')] += 1
50
51            diffAB = count[0] - count[1]
52            diffAC = count[0] - count[2]
53
54            if (diffAB, diffAC) in diff_map:
55                ans = max(ans, i - diff_map[(diffAB, diffAC)])
56            else:
57                diff_map[(diffAB, diffAC)] = i
58
59        return ans