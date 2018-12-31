class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                l = [nums[i], nums[j], nums[k]]
                print(l)
                if sum(l) == 0:
                    res.append(l)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum(l) > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
            # print(i, nums[i])
        return res

print(Solution().threeSum([0, 1, 2, -1]))