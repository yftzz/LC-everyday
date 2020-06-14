class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s) // 2):
            tmp = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = s[i]
            s[i] = tmp
            