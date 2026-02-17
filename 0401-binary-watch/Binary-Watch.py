1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        
4        ans = []
5        for hour in range(12):
6            for minute in range(60):
7                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
8                    ans.append(f"{hour}:{minute:02d}")
9        
10        return ans