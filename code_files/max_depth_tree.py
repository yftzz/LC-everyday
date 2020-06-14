# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    def maxDepth(self, root):
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        return depth(root)
