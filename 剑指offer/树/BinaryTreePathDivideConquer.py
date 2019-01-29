"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        paths = []        
        if root is None:
            return paths

        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)

        for path in left_paths:
            paths.append(str(root.val) + '->' + path)
        for path in right_paths:
            paths.append(str(root.val) + '->' + path)

        # 如果节点是叶子节点
        if len(paths) == 0:
            paths.append(str(root.val))
        return paths

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
    print(Solution().binaryTreePaths(root))