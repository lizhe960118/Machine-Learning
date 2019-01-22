# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = Queue()
        if root is None:
            return []
        q.put(root)
        flag = -1
        s = []
        while not q.empty():
            l = []
            new_q = Queue()
            for node in q:
                l.append(node.val)
                if node.left:
                    new_q.put(node.left)
                if node.right:
                    new_q.put(node.right)
            if flag == -1:
                s.append(l)
            if flag == 1:
                s.append(l[::-1])
            q = new_q
            flag *= -1
        return s