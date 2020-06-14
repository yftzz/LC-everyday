# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    def reverseList(self, head):
        if not head:
            return head

        def rev(node):
            if not node.next:
                return node
            new_head = rev(node.next)
            node.next.next = node
            return new_head
        new_head = rev(head)
        head.next = None
        return new_head

    def improved_rec(self, head):
        def rev(node, prev=None):
            if not node:
                return prev
            ptr = node.next
            node.next = prev
            return rev(ptr, node)
        return rev(head)

    def improved_iter(self, head):
        prev = None
        while head:
            ptr = head.next
            head.next = prev
            prev = head
            head = ptr
        return prev
