class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def inorderNoRecursion(self, root):
        # 左，根，右
        result = []
        if root is None:
            return result

        stack = []
        # stack.append(root)
        cur = root

        while (cur or stack):
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
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
    print(Solution().inorderNoRecursion(root))