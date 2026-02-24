1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
9        def in_order(node):
10            if node == None:
11                return []
12            
13            left_result = in_order(node.left)
14            right_result = in_order(node.right)
15            result = left_result + right_result
16            result = [f"{node.val}{i}"for i in result] or [f"{node.val}"]
17            return result
18
19        result = in_order(root)
20        return sum([int(i, 2) for i in result])
21