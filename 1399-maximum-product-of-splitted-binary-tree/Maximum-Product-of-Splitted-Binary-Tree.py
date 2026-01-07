1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxProduct(self, root: Optional[TreeNode]) -> int:
9        
10        sub_tree_sum_list = []
11
12        def post_order_sum(node):
13            if node == None:
14                return 0
15            
16            left_order_sum = post_order_sum(node.left)
17            right_order_sum = post_order_sum(node.right)
18            sub_tree_sum = left_order_sum + right_order_sum + node.val
19            sub_tree_sum_list.append(sub_tree_sum)
20            return sub_tree_sum
21
22        post_order_sum(root)
23        total_sum = sub_tree_sum_list[-1]
24                
25        max_product = 0
26        for sub_sum in sub_tree_sum_list:
27            product = sub_sum * (total_sum - sub_sum)
28            max_product = max(max_product, product)
29
30        return max_product % (10**9 + 7)