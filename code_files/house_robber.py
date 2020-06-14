class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        return max(self.rob(nums[1:]), nums[0] + self.rob(nums[2:]))

    # ------------ Improved ------------
    def rob(self, nums):
        if not nums:
            return 0
        pprev = 0
        prev = nums[0]
        curr_max = prev
        for i in range(1, len(nums)):
            curr_max = max(pprev + nums[i], prev)
            pprev = prev
            prev = curr_max
        return curr_max
