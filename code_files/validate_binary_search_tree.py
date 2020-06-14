# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    def isValidBST(self, root):
        self.tmp = -float('inf')
        return self.check(root)
    def check(self, node):
        if not node:
            return True
        result = self.check(node.left)
        result = result and self.tmp < node.val
        self.tmp = node.val
        result = result and self.check(node.right)
        return result
    def improved(self, root):
        def check(node, lbound, ubound):
            if not node:
                return True
            return all([check(node.left, lbound, node.val),
                        check(node.right, node.val, ubound),
                        node.val > lbound,
                        node.val < ubound])
        return check(root, -float('inf'), float('inf'))

