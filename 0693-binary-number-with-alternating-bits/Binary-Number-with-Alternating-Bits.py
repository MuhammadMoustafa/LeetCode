1class Solution:
2    def hasAlternatingBits(self, n: int) -> bool:
3        digits = bin(n)
4        for i in range(3, len(digits)):
5            if digits[i] == digits[i-1]:
6                return False
7
8        return True