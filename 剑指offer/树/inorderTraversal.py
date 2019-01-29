"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
class Solution:
    def inorderTraversal(self, root):
        # 左，根，右
        result = []
        if root is None:
            return result
        return self.inorderHelper(root, result)
        
    def inorderHelper(self, root, result):
        if root is None:
            return        
        self.inorderHelper(root.left, result)
        result.append(root.val)
        self.inorderHelper(root.right, result)
        return result

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    root = node1
    print(Solution().inorderTraversal(root))