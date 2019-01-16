class Solution:
    def findMiddle(self, nums1, nums2):
        # 给定两个排好序的数组，编写一个函数来计算它们的中位数。
        # 两个指针分别从nums1、nums2前进，总共前进middle位
        i = 0
        j = 0

        n1 = len(nums1)
        n2 = len(nums2)
        middle = (n1 + n2) // 2
        # 不考虑边界

        ans = -1
        found = 0

        while(i < n1 and j < n2):
            if nums1[i] < nums2[j]:
                i += 1
                if i + j == middle:
                    ans = nums1[i]
                    found = 1
            else:
                j += 1
                if i + j == middle:
                    ans = nums2[j]
                    found = 1

            if found:
                break

        return ans
