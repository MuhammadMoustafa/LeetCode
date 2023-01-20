# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isSorted(l):
            for i in range (1, len(l)):
                if l[i] <= l[i-1]:
                    return False
            return True

        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            result.append(root.val)
            inOrder(root.right)

        result = []
        inOrder(root)
        return isSorted(result)