class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        self.stack.append(number)
        if len(self.min_stack) == 0:
            self.min_stack.append(number)
        else:        
            if number > self.min_stack[-1]:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(number)
                
    """
    @return: An integer
    """
    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    """
    @return: An integer
    """
    def min(self):
        return self.min_stack[-1]
