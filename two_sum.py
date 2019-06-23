class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        vals = {}
        for i in range(len(nums)):
            if target-nums[i] not in vals:
                vals[nums[i]]=i
            else:
                return [vals[target-nums[i]],i]