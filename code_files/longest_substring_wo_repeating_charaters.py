class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        max_len = 1
        idx = 0
        for i in range(len(s)):
            while s[i] in s[idx:i]:
                idx = idx + 1
            max_len = max(max_len, i - idx + 1)
        return max_len