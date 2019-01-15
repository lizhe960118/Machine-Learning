class Solution:
    def threeSum(self, nums, target):
        # 先排序,固定一个数然后移动之后两个指针，接下来要解决重复情况
        n = len(nums)
        if n <= 2:
            return []
        
        nums.sort()

        ret = []
        for i in range(n - 2):

            t = 0 - nums[i]
            
            # 给第一个数去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l_left = i + 1
            l_right = n - 1
            while l_left < l_right:
                s = nums[l_left] + nums[l_right]
                if s < t:
                    l_left += 1
                elif s > t:
                    l_right -= 1
                else:
                    ret.append([nums[i], nums[l_left], nums[l_right]])
                    l_left += 1
                    # 给第二个数去重
                    while nums[l_left] == nums[l_left - 1] and l_left < l_right:
                        l_left += 1

        return ret