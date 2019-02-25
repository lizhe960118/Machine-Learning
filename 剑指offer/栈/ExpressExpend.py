class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # 将s中元素依次入栈，碰到“]”，则出栈至‘[’, 并出栈前一个，如果是数字则翻倍
        stack = []
        
        res = ""
        count = 0

        for i in range(len(s)):
            cur_char = s[i:i+1]
            # char是字母
            if ord("a") <= ord(cur_char) <= ord("z") or ord("A") <= ord(cur_char) <= ord("Z"):
                if len(stack) == 0:
                    stack.append(cur_char)
                else:
                    if stack[-1] != '[':
                        pop_str = stack.pop()
                        pop_str += cur_char
                        stack.append(pop_str)
                    else:
                        stack.append(cur_char)
                    
            # char是数字
            if ord("0") <= ord(cur_char) <= ord("9"):
                if i == 0:
                    stack.append(cur_char)
                else:
                    if (ord("0") > ord(s[i-1:i])) or (ord(s[i-1:i]) >= ord("9")): 
                        stack.append(cur_char)
                    else:
                        number_str = stack.pop()
                        number_str += cur_char
                        stack.append(number_str)
                    
            if cur_char == "[":
                count += 1
                stack.append(cur_char)
                
            if cur_char == "]":
                tmp_str = stack.pop()

                while stack[-1] != '[':
                    tmp_str = stack.pop() + tmp_str
                
                stack.pop()
                count -= 1
                
                if len(stack) != 0 and ord("0") <= ord(stack[-1][-1]) <= ord("9"):
                    number = int(stack.pop())
                    duplicate_tmp = ""
                    for i in range(number):
                        duplicate_tmp += tmp_str
                    stack.append(duplicate_tmp)
            
        return "".join(stack)