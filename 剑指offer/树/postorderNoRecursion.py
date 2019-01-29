"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def postorderNoRecursion(self, root):
        result = []
        if root is None:
            return result
        
        stack = []
        cur = root
        visited = None # 使用visited标记最后访问的右节点
        
        while cur or stack:# stack 非空
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack[-1] # 取cur为最后一个节点，但是不出栈
                if cur.right and cur.right != visited:
                    cur = cur.right
                else:
                    result.append(cur.val)
                    visited = cur
                    stack.pop()
                    cur = None
        return result

    def postorderNoRecursionII(self, root):
        result = []

        if root is None:
            return result

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            result.insert(0, node.val) # result逆序增加元素
            # 添加顺序为，根、右、左，左节点先进栈
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

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
    print(Solution().postorderNoRecursion(root))
    print(Solution().postorderNoRecursionII(root))