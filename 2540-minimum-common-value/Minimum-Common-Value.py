1class Solution:
2    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
3        n1, n2 = len(nums1), len(nums2)
4        idx1, idx2 = 0, 0
5
6        while idx1 < n1 and idx2 < n2:
7            val1, val2 = nums1[idx1], nums2[idx2]
8
9            if val1 == val2:
10                return val1
11
12            if val1 < val2:
13                idx1 += 1
14            else:
15                idx2 += 1
16
17        return -1
18