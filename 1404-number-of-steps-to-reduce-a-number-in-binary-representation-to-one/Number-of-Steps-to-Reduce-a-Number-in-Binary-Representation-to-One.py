1class Solution:
2    def numSteps(self, s: str) -> int:
3        steps = 0
4        num = int(s, 2)
5        print(num)
6        while num != 1:
7            if num % 2 == 0:
8                num //= 2
9            else:
10                num += 1
11            steps += 1
12
13        return steps 