class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
    
        def max_sub(nums, acc):
            if not nums:
                return 0
            if acc:
                return max(0, nums[0] + max_sub(nums[1:], acc = True))
            else:
                return max(max_sub(nums[1:], acc = False), nums[0] + max_sub(nums[1:], acc = True))
        a = max(nums)
        return max_sub(nums, acc=False) if a >0 else a
    


    # -----improved-----
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)
        