1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def post_traversal(node):
10            if node == None:
11                return 0, True
12            left_height, result_left = post_traversal(node.left)
13            right_height, result_right = post_traversal(node.right)
14            result = abs(left_height - right_height) <= 1 and result_left and result_right
15            return max(left_height, right_height) + 1, result
16
17        _, result = post_traversal(root)
18        return result