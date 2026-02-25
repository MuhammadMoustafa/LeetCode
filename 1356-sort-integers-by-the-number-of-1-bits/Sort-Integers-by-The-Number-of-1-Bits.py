1class Solution:
2    def sortByBits(self, arr: List[int]) -> List[int]:        
3        return [int(num, 2) for num in sorted([format(num, '014b') for num in arr], key=lambda x: (x.count('1'), x))]
4