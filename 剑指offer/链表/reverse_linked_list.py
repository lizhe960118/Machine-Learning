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
        prev = None
        cur_node = head

        while(cur_node is not None):
            tmp = cur_node.next # tmp is listNode 保存节点，next在右
            cur_node.next = prev # 更改节点指向，next在左
            # 前进,滞后的指针先前进
            prev = cur_node
            cur_node = tmp
        return prev

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