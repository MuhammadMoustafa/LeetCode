class Solution:
    def climbStairs(self, n: int) -> int:
        return int((((1+(5**(1/2)))/ 2)**(n+1) - (-((1+(5**(1/2)))/ 2))**(-(n+1))) / (5**(1/2)))