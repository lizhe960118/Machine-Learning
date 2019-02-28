"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # sortedListToBSTHelper(self, head, mid)不包含mid
        # sortedListToBSTHelper(mid.next, end.next)
        root = self.sortedListToBSTHelper(head)
        return root
        
    def sortedListToBSTHelper(self, start):
        # 从start排到end，但是不包含end
        # 出口
        if start is None:
            return None
            
        if start.next is None:
            return TreeNode(start.val)
     
        dummy = ListNode(-1)
        dummy.next = start
        
        fast = dummy
        slow = dummy
        
        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
            
        # endNode = None
        # if fast.next is not None:
        #     endNode = fast.next
        # else:
        #     endNode = fast
            
        mid = slow.next
        slow.next = None
        
        root = TreeNode(mid.val)
        root.left = self.sortedListToBSTHelper(start)
        root.right = self.sortedListToBSTHelper(mid.next)
        return root
        
        