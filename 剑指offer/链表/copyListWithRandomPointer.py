"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return head
            
        dummy = RandomListNode(-1)
        
        prev_node = dummy
        new_node = None
        
        # 用来放置节点的对应关系
        d = {}
        
        while(head):
            # copy new_node
            if head in d:
                new_node = d[head]
            else:
                new_node = RandomListNode(head.label)
                d[head] = new_node
            prev_node.next = new_node
            
            # copy random pointer
            if head.random:
                if head.random in d:
                    new_node.random = d[head.random]
                else:
                    new_node.random = RandomListNode(head.random.label)
                    d[head.random] = new_node.random
            
            prev_node = prev_node.next
            head = head.next
            
        return dummy.next