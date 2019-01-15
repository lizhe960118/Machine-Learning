def nSum(nums, N, target, tmp, ret):
    if len(nums) < N or N < 2 or nums[0] * N > target or nums[-1] * N < target:
        return 

    if N == 2:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                ret.append(tmp + [nums[left], nums[right]])
                # 对第二个数进行去重
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    else:
        for i in range(len(nums) - N + 1):
            # 给第一个数去重
            if i > 0 and nums[i] == nums[i-1]:
                continue

            nSum(nums[i+1:], N-1, target - nums[i], tmp + [nums[i]], ret)

def fourSum(nums, target):
    nums.sort()
    N = 4
    tmp = []
    ret = []
    nSum(nums, 4, target, tmp, ret)
    return ret

if __name__ == '__main__':
    print(fourSum([1, 0, -1, 0, -2, 2], 0))