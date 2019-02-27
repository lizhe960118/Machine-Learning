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
        dummy.next= head
        dummy = self.copyLinkedPointer(dummy)
        dummy = self.copyRandomPointer(dummy)

        ret_node = self.splitList(dummy)
        return ret_node

    def copyLinkedPointer(self, dummy):
        # copy linked pointer
        head = dummy.next
        while(head):
            new_node = RandomListNode(head.label)
            tmp = head.next
            head.next = new_node
            new_node.next = tmp 
            head = tmp
        return dummy

    def copyRandomPointer(self, dummy):
        # copy random pointer
        head = dummy.next
        while(head):
            if head.random.next:
                head.next.random = head.random.next
            head = head.next.next 
        return dummy

    def splitList(self, dummy):            
        # 分离链表
        head = dummy.next
        ret_node = head.next
        
        while(head):
            tmp = head.next
            head.next = tmp.next
            head = tmp.next
            if head:
                tmp.next = head.next       
        return ret_node
            