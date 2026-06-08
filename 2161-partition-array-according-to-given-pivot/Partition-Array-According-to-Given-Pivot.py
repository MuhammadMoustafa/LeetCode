1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        less_than_pivot = []
4        equal_pivot = []
5        bigger_than_pivot = []
6
7        for num in nums:
8            if num == pivot:
9                equal_pivot.append(num)
10            elif num > pivot:
11                bigger_than_pivot.append(num)
12            else:
13                less_than_pivot.append(num)
14
15        return less_than_pivot + equal_pivot + bigger_than_pivot
16