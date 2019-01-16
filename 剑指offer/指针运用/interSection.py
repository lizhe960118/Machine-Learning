class Solution:
    def interSection(self, nums1, nums2):
        # 给定两个数组，编写一个函数来计算它们的交集。
        # 思路先排序，然后两个指针分别从nums1、nums2前进，相同则加入ans
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0

        n1 = len(nums1)
        n2 = len(nums2)

        ans = []

        while(i < n1 and j < n2):
            if nums1[i] < nums2[j]:
                i += 1

            elif nums1[i] > nums2[j]:
                j += 1

            else:
                '''
                # 考虑重复的情况：
                if (i > 0 and nums1[i] == nums1[i - 1]) or (j > 0 and nums2[j] == nums2[j - 1]):
                    if (i > 0 and nums1[i] == nums1[i - 1]):
                        i += 1
                    if (j > 0 and nums2[j] == nums2[j - 1]):
                        j += 1
                else:
                    ans.append(nums1[i])
                    i += 1
                    j += 1
                '''
                if (i > 0 and nums1[i] == nums1[i - 1]) or (j > 0 and nums2[j] == nums2[j - 1]):
                    # 由于此时已经有nums1[i] == nums2[j]，他们在之前也保存，直接i+=1, j+=1
                    pass
                else:
                    ans.append(nums1[i])
                i += 1
                j += 1
                
        return ans

if __name__ == '__main__':
    print(Solution().interSection([4,9,5], [9, 4, 9, 8, 4]))