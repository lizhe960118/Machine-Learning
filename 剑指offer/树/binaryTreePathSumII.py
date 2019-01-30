"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import copy

class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def __init__(self, paths=[], path=[]):
        self.paths = []
        self.path = []
        
    def binaryTreePathSum(self, root, target):
        self.pathsHelper(root, target)
        return self.paths

    def pathsHelper(self, root, target):
        if root is None:
            return
        if target == root.val and root.left is None and root.right is None:
            self.path.append(root.val)
            path1 = copy.copy(self.path)
            self.paths.append(path1)
            self.path.pop()
        else:
            self.path.append(root.val)
            self.pathsHelper(root.left, target - root.val)
            self.pathsHelper(root.right, target - root.val)
            self.path.pop()

