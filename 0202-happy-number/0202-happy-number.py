class Solution:
    def isHappy(self, n: int) -> bool:
        number_set = set()
        while n != 1:
            total = 0
            for c in map(int, str(n)):
                total += c*c
            if total in number_set:
                return False
            n = total
            number_set.add(n)
        return True