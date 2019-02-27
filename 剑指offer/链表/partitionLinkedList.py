"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        cur_node = head
        
        node_small = ListNode(-1)
        node_large = ListNode(-1)
        dummy_small = node_small
        dummy_large = node_large
        
        count = 0
        while(cur_node):
            if cur_node.val < x:
                node_small.next = ListNode(cur_node.val)
                node_small = node_small.next
            else:
                node_large.next = ListNode(cur_node.val)
                node_large = node_large.next
            cur_node = cur_node.next
        
        node_small.next = dummy_large.next
        
        return dummy_small.next
        
        