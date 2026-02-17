1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        
4        all_possible_combinations = {}
5        for hour in range(12):
6            for minute in range(60):
7                hour_leds = len([i for i in bin(hour) if i == '1'])
8                minute_leds = len([i for i in bin(minute) if i == '1'])
9                total_leds = hour_leds + minute_leds
10                if total_leds in all_possible_combinations:
11                    all_possible_combinations[total_leds].append(f"{hour}:{minute:02d}")
12                else:
13                    all_possible_combinations[total_leds] = [f"{hour}:{minute:02d}"]
14        
15        return all_possible_combinations.get(turnedOn, [])