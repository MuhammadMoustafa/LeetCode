1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        result = None
4        min_dist = float('inf')
5        for letter in letters:
6            diff = ord(letter) - ord(target)
7            if 0 < diff < min_dist:
8                min_dist = diff
9                result = letter
10
11        return result or letters[0]