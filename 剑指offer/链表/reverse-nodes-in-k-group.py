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
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head
        
        #  一个引用
        cur_node = dummy
        while(cur_node):
            cur_node = self.reverseKGroupHelper(cur_node, k)
        
        return dummy.next
    
    def reverseKGroupHelper(self, head, k):
        # head, 1, 2,..., k,k+1
        # head, k,k-1,...,1,k+1
        # 用来转当前位置的k个元素，并返回下一次要翻转位置的前一个节点
        
        # 判断是否有k个：
        count = 0
        tmp_node = head
        
        while(tmp_node and count <= k):
            tmp_node = tmp_node.next
            if tmp_node:
                count += 1
            # 每多一个元素 count += 1
            
        if count < k:
            return None
        
        # 翻转
        cur_node = head.next
        next_node = cur_node.next
        
        # 标记 node1
        node1 = head.next
        count = 1 
        
        while(next_node and count < k):
            tmp = next_node.next
            next_node.next = cur_node
            cur_node = next_node
            next_node = tmp
            count += 1 
        
        # cur_node = node_k
        # next_node = node_k+1 
        head.next = cur_node
        node1.next = next_node
        
        return node1 
        