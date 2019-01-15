def ValidTriangleNumber(nums):
    # 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
    """
    type: nums List[int]
    rtype: int
    """
    n = len(nums)
    if n <= 2:
        return 0

    nums.sort()

    count = 0
    # for i in range(n-2):
    #     left = i + 1
    #     right = n - 1

    #     while left < right:
    #         if nums[i] + nums[left] > nums[right]:
    #             count += right - left
    #             print(i, left, right)
    #             break
    #         else:
    #             left += 1
    #             # 固定最小位的方法不行，
    #             # 因为在2 + 2 = 4的时候，使left+1则错过(2,3,3), 使right-1则错过（2,3,4）

    '''
    使用固定最大位的方法找到所有值
    '''
    for i in range(2, n):
        left = 0
        right = i - 1

        while left < right:
            s = nums[left] + nums[right]
            if s > nums[i]:#满足构成三角形的条件
                count += right - left #(right固定，第二大边固定， 在最大边固定时，所有left都可与之构造三角形)
                print(left, right, i)
                right -= 1 # 换一个right
            else: # 最短边太短
                left += 1

    return count

if __name__ == '__main__':
    print(ValidTriangleNumber([2,2,3,4]))


