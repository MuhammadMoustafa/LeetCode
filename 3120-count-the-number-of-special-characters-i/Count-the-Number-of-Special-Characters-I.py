1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        char_set = set(word)
4        results = 0
5
6        for c in range(ord('A'), ord('Z')+1):
7            if chr(c) in char_set and chr(c+32) in char_set:
8                results += 1
9                
10        return results
11        