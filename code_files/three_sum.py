class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
        	return []
        res = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
        	l = i+1
        	r = len(nums) - 1

        	if i > 0 and nums[i - 1] == nums[i]:
        		continue

        	while l < r:
        		if nums[l] + nums[r] + nums[i] == 0:
        			res.append([nums[l], nums[r], nums[i]])

        			while l < r and nums[l] == nums[l + 1]:
        				l += 1
        			while l < r and nums[r] == nums[r - 1]:
        				r -= 1
	    			l += 1
	    			r -= 1
	    		else:
	    			if nums[l] + nums[r] + nums[i] < 0:
	    				l += 1
	    			else:
	    				r -= 1

        return res