class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        else:
            from sys import maxsize
            msf = -maxsize - 1
            meh = 0
            for i in range(len(nums)):
                meh += nums[i]
                if msf < meh:
                    msf = meh
                if meh < 0:
                    meh = 0
        return msf
