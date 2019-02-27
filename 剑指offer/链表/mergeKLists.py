# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #把所有链表放入数组，排序后建立新链表返回
        res_list = []
        for l in lists:
            while(l):
                res_list.append(l.val)
                l = l.next
        res_list.sort()

        dummy = ListNode(-1)
        head = dummy

        for num in res_list:
            head.next = ListNode(num)
            head = head.next
            
        return dummy.next