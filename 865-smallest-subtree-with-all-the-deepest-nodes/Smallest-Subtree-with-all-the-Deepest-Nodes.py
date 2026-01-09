1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        
10        def postOrder(node: TreeNode) -> int:
11            if node == None:
12                return 0, node
13
14            left_depth, left_node = postOrder(node.left)
15            right_depth, right_node = postOrder(node.right)
16
17            if left_depth == right_depth:
18                return left_depth + 1, node
19            elif left_depth > right_depth:
20                return left_depth + 1, left_node
21            else:
22                return right_depth + 1, right_node
23
24        depth, node = postOrder(root)   
25        return node