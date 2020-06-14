class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """

        # k = k % len(nums)
        # tmp = []
        # l = nums[:k]
        # i = 0
        # for i in range(len(nums)):
        #     if i < k:
        #         tmp.append(nums[(i + k) % len(nums)])
        #         nums[(i + k) % len(nums)] = nums[i]
        #     else:
        #      tmp.append(nums[(i + k) % len(nums)])
        #      nums[(i + k) % len(nums)] = tmp[0]
        #      tmp.pop(0)
        
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[: len(nums) - k]
