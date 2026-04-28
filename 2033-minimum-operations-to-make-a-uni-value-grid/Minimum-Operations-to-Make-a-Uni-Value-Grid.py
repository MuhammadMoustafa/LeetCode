1class Solution:
2    def minOperations(self, grid: List[List[int]], x: int) -> int:
3        nums_array = [num for row in grid for num in row] 
4        result = 0
5
6        nums_array.sort()
7        n = len(nums_array)
8        median = nums_array[n // 2]
9
10        for num in nums_array:
11            if num % x != median % x:
12                return -1
13            result += abs(median - num) // x
14        
15        return result