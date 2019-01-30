"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class ReturnType:
    def __init__(self, is_balanced, depth):
        self.is_balanced = is_balanced
        self.depth = depth

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        result = self.helper(root)
        return result.is_balanced

    def helper(self, root):
        if root is None:
            return ReturnType(True, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)

        result = ReturnType(True, max(left.depth, right.depth) + 1)

        if left.depth - right.depth > 1 or right.depth - left.depth > 1:
            result.is_balanced = False

        if (left.is_balanced != True) or (right.is_balanced != True):
            result.is_balanced = False

        return result

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    root = node1
    print(Solution().isBalanced(root))