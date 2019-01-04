class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        n1 = len(num1)
        n2 = len(num2)
        store = [0 for i in range(n1 + n2)]
        for i in range(n1):
            for j in range(n2):
                store[n1 + n2 - i - j - 2] += (ord(num1[i:i+1]) - ord('0')) * (ord(num2[j:j+1]) - ord('0'))
        result = ""
        for i in range(n1 + n2 - 1):
            store[i+1] += store[i] // 10
            store[i] = store[i] % 10
            result = chr(store[i] + ord('0')) + result
        
        if store[n1 + n2 - 1] != 0:
            result = chr(store[n1 + n2 - 1] + ord('0')) + result
        return result
            