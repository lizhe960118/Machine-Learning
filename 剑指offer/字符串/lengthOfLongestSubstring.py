class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        location = [-1 for i in range(256)]
        index = -1
        for i, v in enumerate(s):
            if location[ord(v)] > index:
                index = location[ord(v)]
            maxLength = max(maxLength, i - index)
            location[ord(v)] = i
        return maxLength