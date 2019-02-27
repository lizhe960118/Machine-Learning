class Solution:
    def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = None
        tmp = None
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        tmp = head
        while(l1 and l2):
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 is not None:
            tmp.next = l1
        if l2 is not None:
            tmp.next = l2
        return head