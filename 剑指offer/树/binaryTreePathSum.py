"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        self.result = []
        path = []
        self.binaryTreePathSumHelper(self, root, target, path)
        return self.result

    def binaryTreePathSumHelper(self, root, target, path):
        if root is None:
            return
        if root.left is None and root.right is None and root.val == target:
            self.result.append(path + [root.val])
        else:
            self.binaryTreePathSumHelper(root.left, target - root.val, path + [root.val])
            self.binaryTreePathSumHelper(root.right, target - root.val, path + [root.val])



