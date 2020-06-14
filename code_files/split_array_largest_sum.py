from collections import defaultdict
class Solution:
    def search(self, i, nums, m, table, cums):
        if len(nums) == 0:
            return 0

        if m == 1:
            return sum(nums[i:])

        if i in table and m in table[i]:
            return table[i][m]

        table[i][m] = float('inf')

        for j in range(i + 1, len(nums) + 1):
            left, right = cums[j] - cums[i], self.search(j, nums, m - 1, table, cums)
            table[i][m] = min(table[i][m], max(left, right))
            if left > right:
                break

        return table[i][m]

    def splitArray(self, nums: List[int], m: int) -> int:
        table = defaultdict(dict)
        cums = [0]
        for x in nums:
            cums.append(cums[-1] + x)
        return self.search(0, nums, m, table, cums)





class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def valid(mid):
            cnt = 0
            current = 0
            for n in nums:
                current += n
                if current>mid:
                    cnt += 1
                    if cnt>=m:
                        return False
                    current = n
            return True

        l = max(nums)
        h = sum(nums)

        while l<h:
            mid = (h+l)//2
            if valid(mid):
                h = mid
            else:
                l = mid+1
        return l