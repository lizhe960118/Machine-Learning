class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = ""
        stack = []
        if len(s) == 0:
            return ""
        s = s.strip()
        for i in range(len(s)):
            if s[i:i+1] != ' ':
                word += s[i]
            else:
                if s[i-1:i] == " ":
                    continue
                else:
                    stack.append(word)
                    word = ""
        stack.append(word)
        word = ""
        result = ""
        if len(stack) == 0:
            return ""
        for i in range(len(stack) - 1):
            result += stack.pop() + " "
        result += stack.pop()
        return result