# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        mid = (right + left) // 2
        while left != right:
            if isBadVersion(mid):
                right = mid
                mid = (right + left) // 2
            else:
                if left == mid:
                    return mid + 1
                left = mid
                mid = (right + left) // 2
        return mid 

    def imporoved(self, n):
        l = 1
        r = n
        mid = (l+r)//2
        while l<=r:
            if firstBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
