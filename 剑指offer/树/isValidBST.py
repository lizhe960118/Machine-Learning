"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class ReturnType:
    def __init__(self, min_val, max_val, is_valid):
        self.min_val = min_val
        self.max_val = max_val
        self.is_valid = is_valid
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        result = self.Helper(root)
        return result.is_valid
    
    def Helper(self, root):
        if root is None:
            return ReturnType(-float('inf'), float('inf'), True)
            
        leftResult = self.Helper(root.left)
        rightResult = self.Helper(root.right)
        
        result = ReturnType(root.val, root.val, True)
        if leftResult.is_valid == False or rightResult.is_valid == False:
            result.is_valid = False
        
        if (root.left and leftResult.max_val >= result.min_val) or (root.right and rightResult.min_val <= result.max_val):
            result.is_valid = False
        else:
            if root.left:
                result.min_val = leftResult.min_val
            if root.right:
                result.max_val = rightResult.max_val
    
        return result