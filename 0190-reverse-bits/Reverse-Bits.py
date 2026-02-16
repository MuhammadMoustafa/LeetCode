1class Solution:
2    def reverseBits(self, n: int) -> int:
3        result = ""
4        while n:
5            result += str(int(n%2))
6            n = n // 2
7        result = result + "0" * (32-len(result))
8        return int(result, 2)
9