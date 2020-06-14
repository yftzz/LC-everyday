class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not srts:
            return ''
        max_length = min([len(x) for x in strs])
        for i in range(max_length):
            ch = strs[0][i]
            for x in strs:
                if x[i] != ch:
                    return strs[0][:i]
        return srts[0][:max_length]

