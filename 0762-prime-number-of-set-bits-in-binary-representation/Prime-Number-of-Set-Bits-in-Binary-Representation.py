1class Solution:
2    def countPrimeSetBits(self, left: int, right: int) -> int:
3        primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
4
5        result = 0
6        for num in range(left, right+1):
7            if num.bit_count() in primes:
8                result += 1
9
10        return result
11