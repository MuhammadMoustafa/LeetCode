1class Solution:
2    def numSteps(self, s: str) -> int:
3        s = list(s)
4        steps = 0
5        while s != ['1']:
6            if s[-1] == '0':
7                s = s[:-1]
8            else:
9                for i in range(len(s)-1, -1, -1):
10                    if s[i] == '1':
11                        s[i] = '0'
12                    else:
13                        s[i] = '1'
14                        break
15                    if i == 0 and s[-1] == '0':
16                        s = ['1'] + s
17            steps += 1
18
19        return steps 