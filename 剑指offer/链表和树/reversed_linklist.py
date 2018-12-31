# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = None
        next_node = None
        while(head is not None):
            next_node = head.next
            head.next = res
            res = head
            head = next_node
        return res

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            tmp = self.reverseList(head.next)
            #将翻转后的链表的最后节点指向head
            head.next.next = head
            #将head指向空,最后使1指向None
            head.next = None
            return tmp