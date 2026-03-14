1from collections import deque
2
3class Solution:
4    def getHappyString(self, n: int, k: int) -> str:
5        
6        q = deque(['a', 'b', 'c']) 
7
8        for i in range(2, n+1):
9            new_q = deque()
10            while q:
11                word = q.popleft()
12                match word[-1]:
13                    case 'a':
14                        new_q.append(word + 'b')
15                        new_q.append(word + 'c')
16                    case 'b':
17                        new_q.append(word + 'a')
18                        new_q.append(word + 'c')
19                    case 'c':
20                        new_q.append(word + 'a')
21                        new_q.append(word + 'b')
22            q = new_q
23
24        if k > len(q):
25            return ""
26
27        happy_strings = list(q)
28        happy_strings.sort()
29        print(happy_strings)
30        return happy_strings[k-1]
31
32        # ## only a and b
33
34        # if n == 1:
35        #     if k > 3:
36        #         return ""
37        #     return chr(ord('a') + k - 1)
38            
39        # happy_strings = []
40        # def two_letters(l1, l2):
41        #     s1 = []
42        #     s2 = []
43        #     for i in range(n):
44        #         s1.append(l1 if i % 2 == 0 else l2)
45        #         s2.append(l2 if i % 2 == 0 else l1)
46        #     return ["".join(s1), "".join(s2)]
47
48
49        # def three_letters(l1, l2, l3):
50        #     s1 = []
51        #     s2 = []
52        #     s3 = []
53        #     s4 = []
54        #     s5 = []
55        #     s6 = []
56
57        #     for i in range(n):
58        #         s1.append(l1 if i % 3 == 0 else l2 if i % 3 == 1 else l3)
59        #         s2.append(l1 if i % 3 == 0 else l3 if i % 3 == 1 else l2)
60        #         s3.append(l2 if i % 3 == 0 else l1 if i % 3 == 1 else l3)
61        #         s4.append(l2 if i % 3 == 0 else l3 if i % 3 == 1 else l1)
62        #         s5.append(l3 if i % 3 == 0 else l1 if i % 3 == 1 else l2)
63        #         s6.append(l3 if i % 3 == 0 else l2 if i % 3 == 1 else l1)
64        #     return ["".join(s1), "".join(s2), "".join(s3), "".join(s4), "".join(s5), "".join(s6)]
65
66
67        # happy_strings = happy_strings + two_letters('a', 'b') + two_letters('a', 'c') + two_letters('b', 'c')
68        # if n >= 3:
69        #     happy_strings = happy_strings + three_letters('a', 'b', 'c')
70
71        # happy_strings.sort()
72        
73        # if k > len(happy_strings):
74        #     return ""
75
76        # return happy_strings[k-1]
77        
78