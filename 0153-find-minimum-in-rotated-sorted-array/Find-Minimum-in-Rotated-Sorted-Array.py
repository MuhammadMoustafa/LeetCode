1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        n = len(nums)
4        if n < 3:
5            return min(nums)
6        left = 0
7        right = n
8        while left < right:
9            mid = (left + right) // 2
10            if mid == n-1 or nums[mid] > nums[mid+1]:
11                print(mid)
12                return nums[(mid+1)%n]
13            if nums[mid] > nums[left]:
14                left = mid
15            else:
16                right = mid
17
18        return nums[(mid+1)%n] 