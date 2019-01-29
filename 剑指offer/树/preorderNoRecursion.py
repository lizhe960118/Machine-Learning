"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def preorderNoRecursion(self, root):
        # 根，左，右
        result = []
        if root is None:
            return result
        
        stack = []
        stack.append(root)
     
        while stack:# stack 非空
            node = stack.pop()
            result.append(node.val)
            # 这里是先把右节点放到栈中，所以左节点先出栈
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
 
        return result

    def preorderNoRecursionII(self, root):
        result = []
        if root is None:
            return result

        stack = []
        cur = root

        while(cur or stack):
            if cur:
                stack.append(cur)
                result.append(cur.val) 
                cur = cur.left
            else:
                cur = stack.pop()
                # result.append(cur.val)
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
    print(Solution().preorderNoRecursionII(root))