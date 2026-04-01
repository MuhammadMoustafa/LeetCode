1class Solution:
2    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
3        
4        n = len(positions)
5        indices = sorted(range(n), key=lambda i: positions[i])
6        stack = []
7
8        for i in indices:
9            if directions[i] == "R":
10                stack.append(i)
11            else:
12                while stack and healths[i] > 0:
13                    top_r = stack[-1]
14                    if healths[top_r] > healths[i]:
15                        healths[top_r] -= 1
16                        healths[i] = 0
17                    elif healths[top_r] < healths[i]:
18                        healths[i] -= 1
19                        healths[top_r] = 0
20                        stack.pop()
21                    else:
22                        healths[i] = 0
23                        healths[top_r] = 0
24                        stack.pop()
25
26        return [h for h in healths if h > 0]
27