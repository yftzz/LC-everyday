class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        import numpy
        return np.binary_repr(int(n))
        # count = 0
        # while n > 0:
        #     if n % 2 == 0:
        #         count += 1
        #     n = n // 2
        # return count
            
        