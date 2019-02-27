"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # 涉及链表的next,这时候需要找v1的前一个节点
        dummy = ListNode(-1)
        dummy.next = head
        
        search_node = dummy
        v1_node = None
        v2_node = None
        while(search_node):
            if search_node.next and search_node.next.val == v1:
                v1_node = search_node.next
            if search_node.next and search_node.next.val == v2:
                v2_node = search_node.next
            if v1_node and v2_node:
                break
            search_node = search_node.next
        
        if v1_node and v2_node:
            v1_node.val = v2
            v2_node.val = v1
            
        return dummy.next
        
            
