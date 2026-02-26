1class Solution:
2    def numSteps(self, s: str) -> int:
3        steps = 0
4        carry = 0
5        
6        # We go from right to left, stopping before the first digit
7        for i in range(len(s) - 1, 0, -1):
8            digit = int(s[i]) + carry
9            
10            if digit == 1:
11                # Odd number: +1 (1 step) and then it becomes even,
12                # so we divide by 2 (1 step). Total 2 steps.
13                # Adding 1 creates a carry for the next position.
14                steps += 2
15                carry = 1
16            elif digit == 0:
17                # Even number: just divide by 2 (1 step)
18                steps += 1
19                carry = 0
20            elif digit == 2:
21                # This was a '1' that received a carry:
22                # It's now '10', so it's even. Divide by 2 (1 step).
23                # The carry remains 1.
24                steps += 1
25                carry = 1
26                
27        return steps + carry