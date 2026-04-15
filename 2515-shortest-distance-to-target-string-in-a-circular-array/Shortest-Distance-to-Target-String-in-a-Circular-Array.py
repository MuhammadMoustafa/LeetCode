1class Solution:
2    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
3        n = len(words)
4        result = float('inf')
5        for i in range(n):
6            if words[i] == target:
7                abs_path = abs(i - startIndex)
8                result = min(result, abs_path, n-abs_path)
9
10        return -1 if result == float('inf') else result