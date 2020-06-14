class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = len(nums) // 2
        if nums[mid] == target:
        	return mid
        if nums[mid] < nums[-1]: # head on the left
        	if nums[mid] < target and nums[mid] < target[-1]:
        			return mid + self.search(nums[mid + 1:], target)
        	else:
        		return self.search(nums[:mid], target)
        else: # head on the right
        	if nums[mid] > target and nums[0] > target:
        		return mid + self.search(nums[mid + 1:], target)
        	else:
        		return self.search(nums[:mid], target)
