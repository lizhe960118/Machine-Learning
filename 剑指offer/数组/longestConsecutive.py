class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        ans = 0
        for n in set(nums):
            cur_len = 1
            tmp = n + 1
            while tmp in nums_set:
                cur_len += 1
                nums_set.discard(tmp)
                tmp += 1
            tmp = n - 1
            while tmp in nums_set:
                cur_len += 1
                nums_set.discard(tmp)
                tmp -= 1
            ans = max(ans, cur_len)
        return ans