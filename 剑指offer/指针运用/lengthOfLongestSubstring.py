class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)

        res = 0 
        
        left = 0

        d = {}

        for right in range(n):
            if s[right] not in d:
                d[s[right]] = right

            else:
                left = max(left, d[s[right]] + 1) # “abba"第一次b重复，left变为2，下一次a重复，d[a] + 1 < 2,更新left仍为2，即left记录最近一个不重复的位置
                # left = d[s[right]] + 1
                d[s[right]] = right

            if right - left + 1 > res:
                res = right - left + 1
                print(right, left)

        return res

if __name__ == '__main__':
     print(Solution().lengthOfLongestSubstring("abba")) 