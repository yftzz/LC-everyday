class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = dict()
        table[0] = 1
        res = 0
        cum = 0
        for num in nums:
            cum += num
            res += table.get(cum - k, 0)
            table[cum] = table.get(cum, 0) + 1
        return res