class Solution:
    def longestPalindromeSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 最长回文子串，要求子串连续，返回子串
        # bbbab 返回bbb(bab)

        # 1. dp定义
        # 定义dp[i][j]记录子串子串s[i:j+1]是否为回文子串
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]

        # 2.dp初始化 
        # dp[i][i] = 1
        for i in range(n):
            dp[i][i] = 1

        max_len = 0
        start = 0
        end = n - 1
        # 3.dp递推
        for j in range(1, n):
            for i in range(j-1, -1, -1): #注意递推顺序
                if j - i < 2:
                    dp[i][j] == 1 if s[i] == s[j] else 0
                else:
                    if s[i] == s[j]:
                    # 此时结果为子串s[i+1:j-1]是否为回文子串
                        dp[i][j] = dp[i+1][j-1] # 之前的判断是为了防止这里溢出
                    else:
                        dp[i][j] = 0

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
                    end = j + 1

        return s[start:end]

if __name__ == '__main__':
    print(Solution().longestPalindromeSubstring("babad"))