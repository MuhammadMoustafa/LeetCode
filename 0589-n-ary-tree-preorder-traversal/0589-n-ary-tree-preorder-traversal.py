"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        result = []
        def helper(root):
            if root == None:
                return 
            result.append(root.val)
            for child in root.children:
                helper(child)

        helper(root)
        return result