# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = l1
        prev = None

        while l1 and l2:
        	l1.val = l1.val + l2.val + carry
        	carry = l1.val // 10
        	l1.val = l1.val % 10

        	prev = l1
        	l1 = l1.next
        	l2 = l2.next

        while l1:
        	l1.val = l1.val + carry
        	carry = l1.val // 10	
        	l1.val = l1.val % 10

        	prev = l1
        	l1 = l1.next

        if l2:
        	prev.next = l2

        while l2:
        	l2.val = l2.val + carry
        	carry = l2.val // 10
        	l2.val = l2.val % 10

        	prev = l2
        	l2 = l2.next

        if carry == 1:
        	prev.next = ListNode(1)

        return result




class improved_Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = node = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
        	if l1:
        		carry += l1.val
        		l1 = l1.next

        	if l2:
        		carry += l2.val
        		l2 = l2.next

        	carry, val = divmod(carry, 10)
        	node.next = ListNode(val)
        	node = node.next

        return result.next





        