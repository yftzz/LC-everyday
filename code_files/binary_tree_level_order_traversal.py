# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]w
        """
        if not root:
        	return []
        trav = []
        stack = [root]
        while stack:
            trav.append([x.val for x in stack])
            new_stack = []
            for x in stack:
                if x.left:
                    new_stack.append(x.left)
                if x.right:
                    new_stack.append(x.right)
            stack = new_stack
        return trav
