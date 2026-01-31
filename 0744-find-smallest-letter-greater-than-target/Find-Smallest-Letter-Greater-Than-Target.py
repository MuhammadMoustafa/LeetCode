1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        low = 0
4        high = len(letters) - 1
5        
6        # If target is greater than or equal to the last element, 
7        # the answer "wraps around" to the first element.
8        if target >= letters[-1]:
9            return letters[0]
10
11        while low <= high:
12            mid = (low + high) // 2
13            
14            if letters[mid] <= target:
15                low = mid + 1
16            else:
17                high = mid - 1
18        
19        # After the loop, 'low' will point to the smallest element 
20        # strictly greater than the target.
21        return letters[low]