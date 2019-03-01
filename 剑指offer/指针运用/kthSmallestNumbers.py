class Solution:
    def kthSmallestNum(self, nums, k):
        # 返回第k小的数
        if nums is None or len(nums) < k:
            return None 

        result = self.quickSelect(nums, k)
        return result

    def quickSelect(self, nums, k):
        start = 0
        end = len(nums) - 1 
        if start == end:
            return nums[start]

        left = start 
        right = end 

        pivot = nums[start + (end - start) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 

        # 判断
        # ...right, left, ...
        if k - 1 <= right:
            return self.quickSelect(nums[:right + 1], k)
        if k - 1 >= left:
            return self.quickSelect(nums[left:], k - left)
        return nums[k - 1]

if __name__ == '__main__':
    print(Solution().kthSmallestNum([4,3,2,2,1], 4))