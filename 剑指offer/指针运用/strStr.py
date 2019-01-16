class Solution:
    def strStr(self, s, t):
        # 在s中找t第一次出现的位置，不存在返回-1
        if t is None: # t为None则返回0
            return 0
        l_s = len(s)
        l_t = len(t)

        found = 0
        ans = -1

        for i in range(l_s):
            # if s[i] != t[0]:
            #     continue

            for j in range(l_t):
                if s[i + j] != t[j]:
                    break
                else:
                    if j == l_t - 1:
                        ans = i
                        found = 1
                        
            if found: # 跳出大循环
                break

        return ans

if __name__ == '__main__':
    print(Solution().strStr("hello","ll"))
