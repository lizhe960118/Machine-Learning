class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def binaryTreePath(self, root):
        result = []
        if root is None:
            return result
        self.binaryTreePathHelper(root, str(root.val), result)
        return result

    def binaryTreePathHelper(self, root, path, result):
        if root is None:
            return result

        # 叶子节点
        if root.left is None and root.right is None:
            result.append(path)
            return

        # 左节点不空
        if root.left is not None:
            self.binaryTreePathHelper(root.left, path + '->' + str(root.left.val), result)

        if root.left is not None:
            self.binaryTreePathHelper(root.right, path + '->' + str(root.right.val), result)
    

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
    print(Solution().binaryTreePath(root))