from collections import Counter

class Solution:
    def minWindow(self, s, t):
        map_t = Counter(t)
        l_t = len(t)

        fast = 0
        slow = 0
        count = 0
        min_len = len(s)
        index = -1

        n = len(s)

        if n < l_t:
            return ""

        while fast <= n:
            if count < l_t:
                if s[fast:fast+1] in map_t:
                    map_t[s[fast:fast + 1]] -= 1
                    if map_t[s[fast:fast + 1]] >= 0: count += 1
                fast += 1

            else: # 存在满足条件的子串
                if s[slow:slow+1] not in map_t:
                    slow += 1
                    if fast - slow + 1 < min_len:
                        min_len = fast - slow + 1
                        index = slow
                else:
                    if fast - slow <= min_len:
                        min_len = fast - slow
                        index = slow
                    map_t[s[slow:slow + 1]] += 1
                    if map_t[s[slow:slow + 1]] > 0:
                        count -= 1
                    slow += 1

        return s[index:index+min_len] if index >= 0 else ""

    def minWindow_1(self, s, t):
        map_t = Counter(t)

        map_d = dict()        # 另外使用一个字典记录表从i到j字符的出现次数

        slow = 0
        count = 0
        n = len(s)
        min_len = len(s) + 1

        res = ""

        for fast in range(n):
            if s[fast] in map_t:
                map_d[s[fast]] = map_d.get(s[fast], 0) + 1
                if map_d[s[fast]] <= map_t[s[fast]]:
                    count += 1

            if count >= len(t):
                # 存在这样的字符串
                while s[slow] not in map_t or (s[slow] in map_t and map_d[s[slow]] > map_t[s[slow]]):
                    if s[slow] in map_t  and map_d[s[slow]] > map_t[s[slow]]:
                        map_d[s[slow]] -= 1
                    slow += 1  # 移动slow直到满足条件的最短长度

                if fast - slow + 1 < min_len:
                    min_len = fast - slow + 1
                    index = slow
                    res = s[index:index + min_len]

        return res

if __name__ == '__main__':
    print(Solution().minWindow_1("ADOBECODEBANC","ABC"))
    # print(Solution().minWindow("cabwefgewcwaefgcf", "cae"))
    # print(Solution().minWindow("a", "a"))