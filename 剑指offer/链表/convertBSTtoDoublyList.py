"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        if root is None:
            return None
        
        # 前序遍历一次树，左中右
        cur_node = root
        stack = []
        
        array = []
        while(cur_node or stack):
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                array.append(cur_node.val)
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node = None
                    
        prevNode = None
        for i in range(len(array)):
            curNode = DoublyListNode(array[i])
            if prevNode:
                prevNode.next = curNode
                curNode.prev = prevNode
            if i == 0:
                retNode = curNode
            prevNode = curNode
        
        return retNode