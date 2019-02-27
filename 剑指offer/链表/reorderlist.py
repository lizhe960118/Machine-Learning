"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        if head is None or head.next is None:
            return head
            
        # 先找中点，然后把后面的链表翻转，最后拼接
        fast = head
        slow = head
        
        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
        
        # 这样得到前边的链表可能比后面长        
        mid_node = slow.next
        slow.next = None
        
        # 翻转
        prev = None
        cur_node = mid_node
        while(cur_node):
            tmp = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = tmp
        
        # 头结点
        mid_node = prev
        
        # 短的链表先结束
        while(mid_node):
            # 先保存后面未使用的节点
            tmp = mid_node.next
            mid_node.next = head.next
            head.next = mid_node
            head = head.next.next
            mid_node = tmp
        
        return head