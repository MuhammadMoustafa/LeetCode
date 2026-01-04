1class Solution:
2    def sumFourDivisors(self, nums: List[int]) -> int:
3
4        def is_prime(x):
5            if x < 2:
6                return False
7            for i in range(2, round(x**0.5) + 1):
8                if x % i == 0:
9                    return False
10            return True
11        
12        result = 0
13        for num in nums:
14            p = round(num ** (1/3))
15            if is_prime(p) and num == p ** 3:
16                result += 1 + p + p**2 + p**3
17                continue
18
19            for p in range(2, int(num ** 0.5) + 1):
20                if num % p == 0:
21                    q = num // p
22                    if p != q and is_prime(p) and is_prime(q):
23                        result += 1 + p + q + num
24                        break           
25        return result
26        