class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            count = 0
            for j in range(len(needle)):
                if needle[j] == haystack[i + j]:
                    count += 1
                else:
                    break
            if count == len(needle):
                return i
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        return -1
