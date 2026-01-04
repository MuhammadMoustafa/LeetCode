1class Solution:
2    def sumFourDivisors(self, nums: List[int]) -> int:
3
4        results = 0
5        for num in nums:
6            divisors = set([1, num])
7            for i in range(2, int(num**0.5 + 1)): 
8                if num % i == 0:
9                    divisors.add(i)
10                    divisors.add(num // i)
11
12                if len(divisors) > 4:
13                    break
14
15            if len(divisors) == 4:
16                results += sum(divisors)
17
18        return results
19        