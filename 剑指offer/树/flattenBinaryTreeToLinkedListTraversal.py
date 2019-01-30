"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def __init__(self, lastNode = None):
        self.lastNode = lastNode

    def flatten(self, root):
        if root is None:
            return

        if self.lastNode is not None:
            self.lastNode.right = root
            self.lastNode.left = None

        self.lastNode = root
        rightNode = root.right # copy root.right
        self.flatten(root.left)
        self.flatten(rightNode)
        return root

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    root = node1
    print(Solution().flatten(root))