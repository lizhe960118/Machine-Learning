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
        if root is None:
            return root

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

            # connect left to right 
            node.left = None
            if stack:
                node.right = stack[-1]
            else:
                node.right = None
                
        return root

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    root = node1
    print(Solution().flatten(root))