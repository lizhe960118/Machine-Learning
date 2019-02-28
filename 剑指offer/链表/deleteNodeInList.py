"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: the node in the list should be deletedt
    @return: nothing
    """
    def deleteNode(self, node):
        if node is None or node.next is None:
            return 
        
        # 由于没有前节点，我们需要将下一节点的值复制给node，并将下一节点删除
        
        node.val = node.next.val
        
        # 删除下一节点
        next_node = node.next
        node.next = node.next.next
        next_node.next = None
        
