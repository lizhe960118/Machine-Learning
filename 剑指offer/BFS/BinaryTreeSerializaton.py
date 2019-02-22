"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if root is None:
            return '{}'
        
        q = [root]
        index = 0
        
        while index < len(q): # 如果当前节点是空，则其子节点不加入到队列中
            if q[index] is not None:
                q.append(q[index].left)
                q.append(q[index].right)
            index += 1
        
        while q[-1] is None:
            q.pop()
        
        # for node in q:
        #     if node is not None:
        #         print(node.val)
        #     else:
        #         print("#")
            
        result = '{%s}' % ','.join([str(node.val) if node is not None else '#' for node in q])
        
        return result       

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        if data is None:
            return None
            
        data = data.strip('\n')
        
        if data == '{}':
            return None
        
        vals = data[1:-1].split(',')
        
        root = TreeNode(int(vals[0]))
        q = [root] # 使用队列保存节点
        isLeft = True
        index = 0
        
        for val in vals[1:]:
            if val is not "#":
                node = TreeNode(int(val)) 
                if isLeft:
                    q[index].left = node
                else:
                    q[index].right = node
                q.append(node)
                
            if not isLeft:
                index += 1 
            
            isLeft = not isLeft
        
        return root