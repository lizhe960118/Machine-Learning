class Solution:
    def twoSum(self, arr, target):
        # 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
        # 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。（index不是从零开始的）
        arr_length = len(arr)
        if arr_length <= 1:
            return []
        l_left = 0
        l_right = arr_length - 1
        ret = []
        while(l_left < l_right):
            if arr[l_left] + arr[l_right] < target:
                l_left += 1
            elif arr[l_left] + arr[l_right] > target:
                l_right -= 1
            else:
                ret.append(l_left + 1)
                ret.append(l_right + 1)
                break
        return ret 

# 拓展：序列不一定有序（字典解决）
class Solution:
    def twoSum(self, arr, target):
        n = len(arr)

        dict_use = {}

        ret = []

        for i in range(n):
            if arr[i] not in dict_use:# arr[i] is the key, so put (target - arr[i]) in dict
                dict_use[target - arr[i]] = i # value is index
            else:
                ret.append(dict_use[arr[i]])
                ret.append(i)
                break
                
        return ret

