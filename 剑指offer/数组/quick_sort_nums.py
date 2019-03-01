def quick_sort(arr):
    return quickSortHelper(arr, 0, len(arr) - 1)

def quickSortHelper(arr, start, end):
    if start >= end:
        return
        
    pivot = arr[start + (end - start) // 2]
    
    left = start
    right = end

    while left <= right:
        while arr[right] > pivot  and left <= right:
            right -= 1
        while arr[left] < pivot and left <= right:
            left += 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    
    quickSortHelper(arr, start, right)
    quickSortHelper(arr, left, end)
    return arr

print(quick_sort([3,2,1,6,5,4]))


"""
def quick_sort_nums(nums):
    if nums is None or len(nums) == 0:
        return []
    start = 0
    end = len(nums) - 1
    quickSortHelper(nums, start, end)
    return nums

def quickSortHelper(nums, start, end):
    # 判断出口
    if start >= end:
        return

    # 选择标杆
    mid = start + (end - start) // 2
    pivot = nums[mid]

    # 标记左右指针
    left = start
    right = end

    # 直到left移到右边
    while left <= right:
        # 左指针找到第一个大于等于pivot的数
        while nums[left] < pivot and left <= right:
            left += 1
        while nums[right] > pivot and left <= right:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            # 交换之后注意left,right仍要移动
            left += 1
            right -= 1

    quickSortHelper(nums, start, right)
    quickSortHelper(nums, left, end)
    return

print(quick_sort_nums([1, 3, 2, 5, 4]))
"""