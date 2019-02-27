class MyQueue:
    
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        self.stack_1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        self.top()
        return self.stack_2.pop()
    """
    @return: An integer
    """
    def top(self):
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        return self.stack_2[-1]
