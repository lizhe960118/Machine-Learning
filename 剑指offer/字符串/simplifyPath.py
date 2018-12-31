class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        stack = []
        for s in path:
            if s == "." or s == "":
                continue
            if s == "..":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(s)
        if len(stack) == 0:
            return '/'
        result = ""
        for i in range(len(stack)):
            result = '/' + stack.pop() + result
        return result
        