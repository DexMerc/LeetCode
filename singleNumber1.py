class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i<len(nums):
            if i+1<len(nums):
                if nums[i] != nums[i+1]:
                    return nums[i]
            else:
                return nums[i]
            i+=2
        