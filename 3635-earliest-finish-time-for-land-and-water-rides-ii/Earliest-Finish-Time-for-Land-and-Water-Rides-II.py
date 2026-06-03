1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3
4        def get_min_finish_time(x1Start, x1Duration, x2Start, x2Duration):
5            min_finish_time = min(s1 + d1 for s1, d1 in zip(x1Start, x1Duration))
6            return min(max(min_finish_time, s2) + d2 for s2, d2 in zip(x2Start, x2Duration))
7
8
9        min1 = get_min_finish_time(landStartTime, landDuration, waterStartTime, waterDuration)
10        min2 = get_min_finish_time(waterStartTime, waterDuration, landStartTime, landDuration)
11        
12        return min(min1, min2)