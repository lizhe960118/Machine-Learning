class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.helper(s, [], res)
        return res
    def helper(self, s, path, res):
        if len(s) > (4 - len(path)) * 3:
            return
        if len(s) == 0 and len(path) == 4:
            res.append(".".join(path))
            return
        for i in range(min(3, len(s))):
            cur = s[:i+1]
            if (cur[0] == "0" and len(cur)>=2) or int(cur) > 255:
                continue
            self.helper(s[i+1:], path + [s[:i+1]], res)

print(Solution().restoreIpAddresses("25525501"))