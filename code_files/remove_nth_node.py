# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    def removeNthFromEnd(self, head, n):
        def helper(node):  # assume that n is greater than length of list, and list is of length greater than 1
            if not node:
                return 0
            index = helper(node.next) + 1
            if index > n:
                # node.next = node.next.next gonna be crashed, if do so, all
                # nodes will point to n-th node
                node.next.val = node.val
            return index
        helper(head)
        return head.next

    # assume that n is greater than length of list, and list is of length
    # greater than 1
    def improved(self, head, n):
        def helper(node):
            if not node:
                return 0, node
            i, node.next = helper(node.next)
            return i + 1, (node, node.next)[i + 1 == n]
        i, node = helper(head)
        return node
