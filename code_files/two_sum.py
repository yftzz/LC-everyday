class Solution:
    def twoSum(self, nums, target):
        result = {}
        for i in range(len(nums)):
        	if nums[i] in result:
        		return [result[nums[i]], i]
        	else:
        		result[target - nums[i]] = i
        return []        
