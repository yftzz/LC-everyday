class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # pivotal = 0
        count = float('inf')
        lower = []
        higher = []
        curr = nums
        pivotal = len(curr) // 2
        while 1:
            count = 0
            for i in range(len(curr)):
                if i == pivotal:
                    continue
                if curr[i] <= curr[pivotal]:
                    lower.append(curr[i])
                else:
                    higher.append(curr[i])
            if len(higher) == k - 1:
                return curr[pivotal]
            elif len(higher) > k - 1:
                curr = higher
            else:
                k -= (len(higher) + 1)
                curr = lower
            pivotal = len(curr) // 2
            higher = []
            lower = []

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        for _ in range(len(nums) - k + 1):
            res = heapq.heappop(nums)
        return res

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        pivotal = int(random.random()*len(nums))
        
        l = [nums[i] for i in range(len(nums)) if nums[i] <= nums[pivotal] and i != pivotal]
        r = [nums[i] for i in range(len(nums)) if nums[i] > nums[pivotal] and i != pivotal]
        if len(r) == k - 1:
            return nums[pivotal]
        elif len(r) > k - 1:
            return self.findKthLargest(r, k)
        else:
            return self.findKthLargest(l, k - len(r) - 1)
        