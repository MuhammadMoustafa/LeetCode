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
11        total_sum = 0
12
13        def post_order_sum(node):
14            if node == None:
15                return 0
16            
17            nonlocal total_sum
18            left_order_sum = post_order_sum(node.left)
19            right_order_sum = post_order_sum(node.right)
20            sub_tree_sum = left_order_sum + right_order_sum + node.val
21            sub_tree_sum_list.append(sub_tree_sum)
22            return sub_tree_sum
23
24        post_order_sum(root)
25
26        total_sum = sub_tree_sum_list[-1]
27        left_mul = 0
28        right_mul = total_sum
29        min_diff = total_sum
30        
31        
32        for sub_sum in sub_tree_sum_list:
33            new_left_mul = sub_sum
34            new_right_mul = total_sum - sub_sum
35            new_min_diff = abs(new_left_mul - new_right_mul)
36            if new_min_diff < min_diff:
37                min_diff = new_min_diff
38                left_mul = new_left_mul
39                right_mul = new_right_mul
40
41        left_mul = left_mul % (10**9 + 7)
42        right_mul = right_mul % (10**9 + 7)
43        return (left_mul * right_mul) % (10**9 + 7)
44
45        # left_mul = 0
46        # right_mul = total_sum
47        # min_diff = total_sum
48        # for el in sub_tree_sum_list:
49        #     new_left_mul = left_mul + el.val
50        #     new_right_mul = right_mul - el.val
51        #     new_min_diff = new_right_mul - new_left_mul
52        #     print(f"el val = {el.val}, min_diff = {min_diff}, new_min_diff = {new_min_diff}")
53        #     if abs(new_min_diff) < min_diff:
54        #         left_mul = new_left_mul
55        #         right_mul = new_right_mul
56        #         min_diff = new_min_diff
57        #         print(f"left_mul = {left_mul}, right_mul = {right_mul}\n")
58        #     else:
59        #         break
60
61        
62        # left_mul = left_mul % (10**9 + 7)
63        # right_mul = right_mul % (10**9 + 7)
64        # return (left_mul * right_mul) % (10**9 + 7)
65        
66