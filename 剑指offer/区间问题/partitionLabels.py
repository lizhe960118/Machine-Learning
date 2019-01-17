# 字符串 S 由小写字母组成。
# 我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。
# 返回一个表示每个字符串片段的长度的列表。

class Solution:
    def partitionLabels(self, s):
        d = {}
        # 使用字典d记录每个字符出现的最高位
        n = len(s)
        for i in range(n):
            d[s[i]] = i

        right = 0
        left = 0
        ans = []

        for i in range(n):
            right = max(right, d[s[i]])

            if right == i:# 说明可以分段了
                ans.append(right - left + 1)
                left = right + 1

        return ans