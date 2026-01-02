1class Solution:
2    def repeatedNTimes(self, nums: List[int]) -> int:
3        
4        result_dict = dict()
5        for num in nums:
6            if num in result_dict:
7                result_dict[num] += 1
8
9                if result_dict[num] == len(nums) / 2:
10                    return num
11            
12            else:
13                result_dict[num] = 1
14        