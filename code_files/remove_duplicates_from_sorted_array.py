class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)


# -------------------- My improved --------------------
    def removeDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            count = 0
            curr_int = float('inf')
            for i in range(len(nums)):
                if nums[i] != curr_int:
                    curr_int = nums[i]
                    nums[count] = curr_int
                    count += 1
            return count