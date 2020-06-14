class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        head = lh = len(nums) - 1

        while head > 0 and nums[head - 1] >= nums[head]:
            head -= 1
        if head == 0:
            nums.reverse()
            return None
        k = head - 1
        while nums[k] >= nums[lh] and lh > head:
            lh -= 1
        nums[k], nums[lh] = nums[lh], nums[k]
        l, r = head, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1