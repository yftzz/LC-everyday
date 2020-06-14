# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.isLocalSymm(root.left, root.right)
        return True

    def isLocalSymm(self, l, r):
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False

        if l.val == r.val:
            return self.isLocalSymm(
                l.left, r.right) and self.isLocalSymm(
                l.right, r.left)
        return False
