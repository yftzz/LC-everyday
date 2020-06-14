class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.get_k(nums1, nums2, l // 2)
        else:
            return (self.get_k(nums1, nums2, l // 2) + self.get_k(nums1, nums2, l // 2 - 1)) / 2.0

    def get_k(self, A,B,k):
        if not A:
            return B[k]
        if not B:
            return A[k]

        ia = len(A) // 2
        ib = len(B) // 2

        ma = A[ia]
        mb = B[ib]

        if ia + ib < k:
            if ma > mb:
                return self.get_k(A, B[ib + 1:], k - ib - 1)
            else:
                return self.get_k(A[ia + 1:], B, k - ia - 1)
        else:
            if ma > mb:
                return self.get_k(A[:ia], B, k)
            else:
                return self.get_k(A, B[:ib], k)