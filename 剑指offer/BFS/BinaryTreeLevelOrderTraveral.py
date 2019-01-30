"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from queue import Queue

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if root is None:
            return []

        q = Queue()
        q.put(root)

        result = []
        
        while not q.empty(): # 注意结束条件
            size = q.qsize()
            level = [] # level初始化
            for i in range(size):
                node = q.get()
                level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            print(level)
            result.append(level)
        return result

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    root = node1
    print(Solution().levelOrder(root))
