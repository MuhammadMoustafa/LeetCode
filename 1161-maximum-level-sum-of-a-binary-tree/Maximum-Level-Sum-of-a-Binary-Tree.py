1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8from collections import deque
9
10class Solution:
11    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
12        max_level = 0
13        max_level_sum = float("-inf")
14        current_level = 1
15        
16        queue = deque([root])
17
18        while queue:
19            level_sum = 0
20            level_length = len(queue)
21
22            for _ in range(level_length):
23                node = queue.popleft()
24                level_sum += node.val
25
26                if node.left:
27                    queue.append(node.left)
28                if node.right:
29                    queue.append(node.right)
30
31            if level_sum > max_level_sum:
32                max_level_sum = level_sum
33                max_level = current_level
34
35            current_level += 1
36
37        return max_level