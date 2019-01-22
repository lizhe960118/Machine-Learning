# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 归并排序，递归处理
        return self.helper(head)
    
    def helper(self, head):
        if head is None or head.next is None:
        	return head
        fast = head
        slow = head
        while (fast.next and fast.next.next):
        	fast = fast.next.next
        	slow = slow.next
        mid = slow.next
        slow.next = None
        l1 = self.helper(head)
        l2 = self.helper(mid)
        node = self.merge(l1, l2)
        return node
    
    def merge(self, l1, l2):
    	if l1 is None:
    		return l2
    	if l2 is None:
    		return l1
    	head = None
    	tmp = None
    	if l1.val <= l2.val:
    		head = l1
    		l1 = l1.next
    	else:
    		head = l2
    		l2 = l2.next
    	tmp = head
    	while(l1 and l2):
            if l1.val <= l2.val:
	    		tmp.next = l1
	    		l1 = l1.next
            else:
	    		tmp.next = l2
	    		l2 = l2.next
            tmp = tmp.next
        if l1 is not None:
            tmp.next = l1
	    if l2 is not None:
	    	tmp.next = l2
	    return head