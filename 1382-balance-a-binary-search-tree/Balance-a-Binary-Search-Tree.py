1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        nodes = []
10        
11        def in_order(node):
12            if node == None:
13                return
14            in_order(node.left)
15            nodes.append(node)
16            in_order(node.right)
17
18        
19        def construct_bst(arr):
20            if not arr:
21                return 
22
23            middle = len(arr) // 2
24            root = arr[middle]
25            
26            root.left = construct_bst(arr[:middle])
27            root.right = construct_bst(arr[middle+1:])
28            
29            return root
30
31        in_order(root)
32        new_root = construct_bst(nodes)
33        return new_root