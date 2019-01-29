"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
class Solution:
    def preorderTraversal(self, root):
        # 根，左，右
        result = []
        if root is None:
            return result
        return self.preorderHelper(root, result)
        
    def preorderHelper(self, root, result):
        if root is None:
            return
        result.append(root.val)
        
        self.preorderHelper(root.left, result)
        self.preorderHelper(root.right, result)
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
    print(Solution().preorderTraversal(root))