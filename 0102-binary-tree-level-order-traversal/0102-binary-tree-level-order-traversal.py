# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        def levelHelper(node, lvl):
            if not node:
                return

            if lvl >= len(result):
                result.append([])
            
            result[lvl].append(node.val) 
            levelHelper(node.left, lvl+1)
            levelHelper(node.right, lvl+1)

        levelHelper(root, 0)
        return result