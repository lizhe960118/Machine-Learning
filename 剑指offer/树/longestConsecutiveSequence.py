"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class ReturnType(object):
    """docstring for ReturnType"""
    def __init__(self, maxInsubtree, maxFromNode):
        # maxInsubtree 从子树返回的最长子序列长度
        # maxFromRoot 当前节点返回的最长子序列长度
        self.maxInsubtree = maxInsubtree
        self.maxFromNode = maxFromNode
        
class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        result = self.helper(root)
        return result.maxInsubtree

    def helper(self, root):
        if root is None:
            return ReturnType(0, 0)
        # divide
        leftResult = self.helper(root.left)
        rightResult = self.helper(root.right)

        result = ReturnType(0, 1)
        # conquer
        if root.left and (root.left.val == root.val + 1):
            result.maxFromNode = max(result.maxFromNode, leftResult.maxFromNode + 1)

        if root.right and (root.right.val == root.val + 1):
            result.maxFromNode = max(result.maxFromNode, rightResult.maxFromNode + 1)

        # 更新result的可能从子树得到的最长连续子串长度
        result.maxInsubtree = max(result.maxFromNode, max(leftResult.maxInsubtree, rightResult.maxInsubtree))

        return result
            
