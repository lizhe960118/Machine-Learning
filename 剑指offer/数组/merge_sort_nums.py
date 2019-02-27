def merge_sort(nums):
    if nums is None or len(nums) == 0:
        return []

    tmp = [0 for i in range(len(nums))]

    mergeSortHelper(nums, 0, len(nums) - 1, tmp)
    return nums

def mergeSortHelper(nums, start, end, tmp):
    if start >= end:
        return
    mid = start + (end - start) // 2
    mergeSortHelper(nums, start, mid, tmp)
    mergeSortHelper(nums, mid+1, end, tmp)
    merge_nums(nums, start, end, tmp)
    return

def merge_nums(nums, start, end, tmp):
    mid = start + (end - start) // 2
    leftIndex = start
    rightIndex = mid + 1
    tmpIndex = start

    while leftIndex <= mid and rightIndex <= end:
        if nums[leftIndex] < nums[rightIndex]:
            tmp[tmpIndex] = nums[leftIndex]
            tmpIndex += 1
            leftIndex += 1
        else:
            tmp[tmpIndex] = nums[rightIndex]
            tmpIndex += 1
            rightIndex += 1

    # 多余没有排序的
    while leftIndex <= mid:
        tmp[tmpIndex] = nums[leftIndex]
        tmpIndex += 1
        leftIndex += 1

    while rightIndex <= end:
        tmp[tmpIndex] = nums[rightIndex]
        tmpIndex += 1
        rightIndex += 1

    for i in range(start, end + 1):
        nums[i] = tmp[i]

    return 

print(merge_sort([1, 3, 2, 5, 4]))