class Solution:
    def subSet(self, nums):
        results = []
        n = len(nums)
        if nums is None or n == 0:
            return results
        nums.sort()
        #使用这个函数来给results添加subset
        self.dfsHelper(nums, 0, [], results)
        return results

    def dfsHelper(self, nums, start_index, subset, results):

        # start_index 记录下以nums[start_index]为首元素的子集
        subset_cp = subset.copy()
        results.append(subset_cp)

        for i in range(start_index, len(nums)):
            subset.append(nums[i])
            self.dfsHelper(nums, i+1, subset, results)
            subset.pop()

if __name__ == '__main__':
    print(Solution().subSet([1, 2, 3]))