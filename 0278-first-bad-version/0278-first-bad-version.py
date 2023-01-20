# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        def b_search(left, right):
            i = (left + right) // 2
            if isBadVersion(i)and not isBadVersion(i-1):
                return i
            if isBadVersion(i):
                return b_search(left, i-1)
            else:
                return b_search(i+1, right)

        return b_search(0, n)