"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if head is None:
            return False
        
        # 快慢指针，快的走两步，慢的走一步
        fast = head
        slow = head
        
        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False