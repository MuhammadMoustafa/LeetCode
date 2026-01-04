class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, round(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        result = 0
        for num in nums:
            p = round(num ** (1/3))
            if is_prime(p) and num == p ** 3:
                result += 1 + p + p**2 + p**3
                continue

            for p in range(2, int(num ** 0.5) + 1):
                if num % p == 0:
                    q = num // p
                    if p != q and is_prime(p) and is_prime(q):
                        result += 1 + p + q + num
                        break           
        return result

### Faster Version

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        results = 0
        for num in nums:
            divisors = set([1, num])
            for i in range(2, int(num**0.5 + 1)): 
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)

                if len(divisors) > 4:
                    break

            if len(divisors) == 4:
                results += sum(divisors)

        return results        
