class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def maximunDepthOfTree(self, root):
        if root is None:
            return 0

        ## 分治算法
        left = self.maximunDepthOfTree(root.left)
        right = self.maximunDepthOfTree(root.right)
        
        depth = max(left, right) + 1
        return depth

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
    print(Solution().maximunDepthOfTree(root))