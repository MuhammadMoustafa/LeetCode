1class Solution:
2    def minimumCost(self, cost: List[int]) -> int:
3        n = len(cost)
4        cost.sort()
5        total = 0
6
7        for i in range(n, -1, -1):
8            if (n - i) % 3 == 0:
9                continue
10            total += cost[i]
11
12        return total