class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ind = len(nums) - 1
        flag = True

       
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= ind:
                ind = i
        return not ind

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i in range(len(nums)):
            if m < i:
                return False
            m = max(m, nums[i] + i)
        return True