"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.next_item = None
        self.stack = []
        for item in reversed(nestedList):
            self.stack.append(item)
        
    # @return {int} the next element in the iteration
    def next(self):
        if self.next_item is None:
            self.hasNext()
        tmp = self.next_item
        self.next_item = None
        return tmp
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # 已经有下一个元素，则不用遍历
        if self.next_item:
            return True
        
        while len(self.stack) != 0:
            top = self.stack.pop()
            
            if top.isInteger():
                self.next_item = top.getInteger()
                return True
            else:
                for item in reversed(top.getList()):
                    self.stack.append(item)
            
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())