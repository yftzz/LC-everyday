# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        flag = True
        dummy = ListNode(0)
        res = dummy
        while flag:
        	flag = False
        	min_ind = -1
        	min_num = float('inf')
        	for i in range(len(lists)):
        		if not lists[i]:
        			continue
        		if lists[i].val < min_num:
        			min_ind = i
        			min_num = lists[i].val
        			flag = True

        	if min_ind >= 0:
        		dummy.next = ListNode(min_num)
        		dummy = dummy.next
        		lists[min_ind] = lists[min_ind].next

        return res.next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        res = dummy

        from queue import PriorityQueue
        q = PriorityQueue()
        for l in lists:
        	if l:
        		q.put((l.val, l))
        while q.qsize() > 0:
        	node = q.get()[1]
        	dummy.next = node
        	dummy = dummy.next
        	if dummy.next:
        		q.put((dummy.next.val, dummy.next))
        return res.next

