1class Solution:
2    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
3
4        result = 0
5        for i in range(len(points)-1):
6            x1, y1 = points[i]
7            x2, y2 = points[i+1]            
8            result += max(abs(x1-x2), abs(y1-y2))
9            
10        return result