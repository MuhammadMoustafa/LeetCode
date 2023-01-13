class Solution:
    def longestPalindrome(self, s: str) -> int:
        letterCount = Counter(s)
        maxOdd = 0
        result = 0
        isOdd = 0
        for count in letterCount.values():
            if count%2 == 0:
                result += count
            else:
                isOdd = 1
                result += count - 1
        return result + maxOdd + isOdd