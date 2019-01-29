class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def postorderTraversal(self, root):
        # 左, 右，根
        result = []
        if root is None:
            return result

        return self.postorderHelper(root, result)

    def postorderHelper(self, root, result):
        if root is None:
            return
            
        self.postorderHelper(root.left, result)
        self.postorderHelper(root.right, result)
        result.append(root.val)
        
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
    print(Solution().postorderTraversal(root))