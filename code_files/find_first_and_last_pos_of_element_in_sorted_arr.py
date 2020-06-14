class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mid = len(nums) // 2
        if nums[mid] != target:
            if nums[mid] < target:
                res = self.searchRange(nums[mid + 1:], target)
                if nums[0] >= 0:
                    res = [x + mid for x in res]
            else:
                res = self.searchRange(nums[:mid], target)
        else:
            l = r = mid
            while l > 0 and nums[l - 1] == target:
                l -= 1
            while r < len(nums) - 1 and nums[r + 1] == target:
                r += 1
            return [l, r]