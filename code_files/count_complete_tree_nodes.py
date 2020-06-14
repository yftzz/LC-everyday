# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
    	if not root:
    		return 0

    	lDepth = self.getDepth(root.left)
    	rDepth = self.getDepth(root.right)

    	if lDepth == rDepth:
    		return 2 ** lDepth + self.countNodes(root.right)
    	else:
    		return 2 ** rDepth + self.countNodes(root.left)


    def getDepth(self, node):
    	if not node:
    		return 0
    	return 1 + self.getDepth(node.left)