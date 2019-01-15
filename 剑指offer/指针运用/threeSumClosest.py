class Solution:
    def threeSumClosest(self, nums, target):
        # 先排序,固定一个数然后移动之后两个指针，每次记录最近目标值的数组，接下来要解决重复情况

        n = len(nums)
        if n <= 2:
            return []
        
        nums.sort()

        s_tmp = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
        
            # 给第一个数去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l_left = i + 1
            l_right = n - 1
            
            while l_left < l_right:
                s = nums[i] + nums[l_left] + nums[l_right]

                dist = abs(t - s_tmp)
                dist_new = abs(t - s)
                if dist_new < dist:
                    s_tmp = s
                    ret = []
                    ret.append([nums[i], nums[l_left], nums[l_right]])

                if s < target:
                    l_left += 1
                elif s > target:
                    l_right -= 1
                else:
                    ret = []
                    ret.append([nums[i], nums[l_left], nums[l_right]])
                    break                    # l_left += 1
                    # # 给第二个数去重
                    # while nums[l_left] == nums[l_left - 1] and l_left < l_right:
                    #     l_left += 1

        return ret