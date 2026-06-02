1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3
4
5        def get_min_finish_time(start1, dur1, start2, dur2):
6            min_finish_time = min(s1 + d1 for s1, d1 in zip(start1, dur1))
7            return min(max(min_finish_time, s2) + d2 for s2, d2 in zip(start2, dur2))
8
9        
10        min1 = get_min_finish_time(landStartTime, landDuration, waterStartTime, waterDuration)
11        min2 = get_min_finish_time(waterStartTime, waterDuration, landStartTime, landDuration)
12        return min(min1, min2)
13        