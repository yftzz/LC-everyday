class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        for i in range(len(nums)):
            res.extend([[nums[i]] + x for x in self.permute(nums[:i] + nums[i + 1:])])
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.bt(nums, [], res)
        return res
        
    def bt(self, nums, comb, res):
        if not nums:
            res.append(comb)

        for i in range(len(nums)):
            self.bt(nums[:i] + nums[i + 1:], [nums[i]]+comb, res)
