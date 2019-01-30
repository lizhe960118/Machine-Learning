"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class ReturnType:
    def __init__(self, cur_sum, min_sum,subtree):
        self.cur_sum = cur_sum
        self.min_sum = min_sum
        self.subtree = subtree

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # result = ReturnType()
        result = self.findSubtreeHelper(root)
        return result.subtree.val

    def findSubtreeHelper(self, root):
        # return ReturnType
        if root is None:
            return ReturnType(0,float('inf'),None)

        left_re = self.findSubtreeHelper(root.left)
        right_re = self.findSubtreeHelper(root.right) 

        result = ReturnType(left_re.cur_sum + right_re.cur_sum + root.val, # 当前值等于left、right返回的和和节点值相加
                            left_re.cur_sum + right_re.cur_sum + root.val, # 假设left、right返回空，这时最小值是节点值本身
                            root)

        if left_re.min_sum <= result.min_sum: 
        # 如果当前算得的最小和 大于 左节点保存的最小和，
        # min_sum起到保存最小和的作用
            result.min_sum = left_re.min_sum
            result.subtree = left_re.subtree

        if right_re.min_sum <= result.min_sum:
            result.min_sum = right_re.min_sum
            result.subtree = right_re.subtree

        return result

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(-5)
    node3 = TreeNode(2)
    node4 = TreeNode(0)
    node5 = TreeNode(2)
    node6 = TreeNode(-4)
    node7 = TreeNode(-5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node4.right = node7
    root = node1
    print(Solution().findSubtree(root))