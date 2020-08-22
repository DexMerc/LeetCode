def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zero_count = 0
    j = 0
    lena = len(nums)
    for i in range(lena):
        if nums[i] == 0:
            print(nums[i], zero_count)
            zero_count += 1
        else:
            if zero_count > 0:
                nums[j] = nums[i]
            j += 1

    if zero_count > 0:
        for i in range(zero_count):
            nums[lena - 1 - i] = 0
