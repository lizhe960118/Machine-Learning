"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        tmp = root
        self.flattenHelper(tmp) # 最后只要实现flatten操作即可
        return root

    def flattenHelper(self, root):
        if root is None:
            return None

        leftLast = self.flattenHelper(root.left)
        # 返回左子树的最后一个节点
        rightLast = self.flattenHelper(root.right)

        # 将左子树和右子树连起来
        if leftLast is not None：
            leftLast.right = root.right
            root.right = root.left
            root.left = None

        # 返回右子树最后一个节点
        if rightLast is not None:
            return rightLast

        # 右子树为空， 返回操作后的左节点
        if leftLast is not None:
            return leftLast

        # leaf node 
        return root




if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    root = node1
    print(Solution().flatten(root))