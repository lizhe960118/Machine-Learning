class Solution:
    def mergeTwoList(self, nums1, nums2):
        # 写代码这里不考虑边界条件
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 <= 0:
            return nums2
        if n2 <= 0:
            return nums1

        for j in range(n2):
            nums1.append(0)

        p = n1 + n2 - 1 # 从0开始，有n1+n2个数
        i = n1 - 1
        j = n2 - 1

        while(i >= 0 and j >= 0):
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
                p -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
                p -= 1 
        # nums2 有剩余
        while(j >= 0):
            nums1[p] = nums2[j]
            j -= 1
            p -= 1
        return nums1

if __name__ == '__main__':
    print(Solution().mergeTwoList([1, 2, 3], [4, 5, 6]))
    print(Solution().mergeTwoList([4, 5, 6], [1, 2, 3]))