1class Solution:
2    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
3        result = []
4        for q in queries:
5            for d in dictionary:
6                changes = 0
7                l = len(q)
8                for i in range(l):
9                    if q[i] != d[i]:
10                        changes += 1
11                        if changes > 2:
12                            break
13                if changes <= 2:
14                    result.append(q)
15                    break
16
17        return result
18