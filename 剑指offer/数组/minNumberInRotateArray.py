# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length == 0:
            return 0
        left = 0
        right = length - 1
        mid = 0
        while(left < right):
            if right - left == 1:
                mid = right
                break
            mid = left + (right - left) // 2
            if rotateArray[mid] <= rotateArray[right]:
                right = mid
            #elif rotateArray[mid] > rotateArray[right]:
            else:
                left = mid
        return rotateArray[mid]