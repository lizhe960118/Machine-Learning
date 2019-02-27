# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        # 算出长链表比短链表多的长度，让长链表多走k步
        if headA is None or headB is None:
            return None
        tmpA = headA
        tmpB = headB
        lenA = 0
        lenB = 0
        while(tmpA):
            tmpA = tmpA.next
            lenA += 1
        while(tmpB):
            tmpB = tmpB.next
            lenB += 1

        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        else:
            for i in range(lenB - lenA):
                headB = headB.next

        while(headA != headB):
            headA = headA.next
            headB = headB.next
        return headA
        